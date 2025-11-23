📻 MyHamDashboard

The "Shack-in-a-Browser" Display for the Modern Operator

Welcome to MyHamDashboard! Because sometimes you want to check propagation conditions, local radar, and solar wind without firing up 15 different browser tabs or buying another Raspberry Pi that you'll definitely configure "someday."

This is a lightweight, single-file HTML dashboard designed to run locally on your machine. It puts the "control" in Mission Control, optimized for Boone County, KY, but ready to be forked for your own QTH.

📡 Features (The "Specs")

The 4x3 Grid of Glory: Displays 12 monitored frequencies... err, images, perfectly sized to your screen. No scrolling required (unless you want to).

Zero-Install Deployment: No Docker containers, no npm install, no compiling kernels. Just download dashboard.html and double-click it like it's 1999.

The Stealth Menu: A stealthy menu button integrated into the ticker bar. It's there when you need it, gone when you're staring at the solar flux index.

The Ticker of Truth: A transparent, floating ticker at the bottom that pulls live NWS weather alerts. It scrolls faster than a contest operator on Red Bull.

Band-Agnostic: Whether you rock a Baofeng or a base station worth more than your car, this dashboard doesn't judge. It supports Ham, GMRS, and Weather enthusiasts alike.

CORS-Fu: Uses clever workarounds (like direct image generators and public JSON proxies) to try and load external content without making your browser scream about security policies.

🛠️ Installation & Usage

Clone the Repo:

git clone [https://github.com/yourusername/MyHamDashboard.git](https://github.com/yourusername/MyHamDashboard.git)


Run It:

Method A (The "I just want it to work" method): Right-click dashboard.html -> Open with Chrome/Edge/Firefox.

Method B (The "I like Python" method): Open a terminal in the folder and run python -m http.server. Then go to localhost:8000.

Enjoy: Watch the clouds move and the solar x-rays spike.

🔧 Customization (Mod Your Rig)

Want to change the location from Boone County to your county?

Open dashboard.html in VS Code (or Notepad if you like pain).

Change the Links: Look for the contentUrls array. Swap my links for your local radar, traffic cams, or cat GIFs.

Change the Ticker: Find const RSS_URL near the bottom. Replace KYZ091 with your own NWS Zone ID.

Change the Name: Find BOONE COUNTY WX and swap it for your call sign or "THE BUNKER."

🤝 Credit & Acknowledgments

My idea for this Dashboard came from VA3HDL/hamdashboard.

I just rewrote the code with the help of Gemini in VSCode to make this Dashboard the way I like it—streamlined, local, and ready for the shack.

📜 License

Feel free to fork it, mod it, break it, and fix it. Just don't broadcast spurious emissions.

73