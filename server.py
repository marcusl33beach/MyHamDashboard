import http.server
import socketserver
import urllib.request
import urllib.parse
import ssl
import os

# Allow overriding the port via the environment variable PORT (useful if 8000 is in use)
PORT = int(os.environ.get('PORT', '8000'))

class CORSRequestHandler (http.server.SimpleHTTPRequestHandler):
    def end_headers (self):
        # Allow simple cross-origin fetches from the dashboard page
        self.send_header('Access-Control-Allow-Origin', '*')
        http.server.SimpleHTTPRequestHandler.end_headers(self)

    def do_GET(self):
        # Provide a very small proxy endpoint to fetch remote pages (useful to bypass CORS
        # and embed external HTML like the hamqsl page). Usage: /proxy?url=<encoded-url>
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == '/proxy':
            qs = urllib.parse.parse_qs(parsed.query)
            url_vals = qs.get('url') or qs.get('target')
            if not url_vals:
                self.send_response(400)
                self.send_header('Content-Type','text/plain; charset=utf-8')
                self.end_headers()
                self.wfile.write(b'Missing url parameter')
                return

            url = url_vals[0]
            try:
                # Robust fetch with retries and common headers to reduce remote rejections
                def fetch_with_retries(target_url, attempts=3, timeout=20):
                    last_exc = None
                    for i in range(attempts):
                        try:
                            ctx = ssl.create_default_context()
                            headers = {
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                                'Accept-Language': 'en-US,en;q=0.5',
                                'Referer': urllib.parse.urlparse(target_url).scheme + '://' + urllib.parse.urlparse(target_url).netloc + '/',
                                'Connection': 'close'
                            }
                            req = urllib.request.Request(target_url, headers=headers)
                            opener = urllib.request.build_opener()
                            with opener.open(req, context=ctx, timeout=timeout) as resp:
                                return resp.read(), resp.getheader('Content-Type')
                        except Exception as e:
                            last_exc = e
                            # small backoff
                            import time
                            time.sleep(0.5 * (i + 1))
                    raise last_exc

                data, ctype = fetch_with_retries(url, attempts=3, timeout=20)
                if not ctype:
                    ctype = 'application/octet-stream'
            except Exception as e:
                # Log full exception server-side for diagnostics
                import traceback
                traceback.print_exc()
                self.send_response(502)
                self.send_header('Content-Type','text/plain; charset=utf-8')
                self.end_headers()
                # Return a clearer error message to the client
                msg = ('Error fetching %s:\n%s' % (url, repr(e))).encode('utf-8')
                self.wfile.write(msg)
                return

            self.send_response(200)
            self.send_header('Content-Type', ctype)
            self.send_header('Access-Control-Allow-Origin','*')
            self.send_header('Cache-Control','no-cache, no-store, must-revalidate')
            self.end_headers()
            self.wfile.write(data)
            return

        return http.server.SimpleHTTPRequestHandler.do_GET(self)

with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
    print(f"serving at port {PORT}")
    httpd.serve_forever()