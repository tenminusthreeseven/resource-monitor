# Resource Monitor - Easy Guide
## What is this?

This is a Python script that watches your computer or server.
It checks CPU usage (how hard your computer is working) and memory usage (how much space your computer is using).

If your computer is working too hard, it will send you an email alert so you can fix it early.

## Features

Checks CPU and memory every 5 minutes.

Sends an email if:

CPU usage > 80%

Memory usage > 75%

Only sends one alert every 12 hours (no spamming!).

Saves logs in server_monitor.log so you can see what happened.

Works on Windows, Linux, and Mac.

What You Need

Python 3.x installed on your computer.
Check by opening a terminal or command prompt and typing:

python3 --version


Install psutil (a Python tool to check CPU and memory):

pip install psutil


## Email setup:

Don’t use your normal email password.

Enable 2-factor authentication on your email account.

Create an app password (this is a special password just for apps).

Remove any spaces from the password before using it in the script.

How to Create & Start the Script
On Linux / Mac

Open Terminal.

Type this command to create a new file:

nano resourcemonitor.py


Paste the Python code into the editor.

Press Ctrl + O to save, then Enter.

Press Ctrl + X to exit.

Run the script:

python3 resourcemonitor.py

## On Windows

Open Notepad (or any text editor like VS Code).

Paste the Python code into a new file.

Save the file as:

resourcemonitor.py


Make sure the extension is .py, not .txt.

Open Command Prompt in the folder where you saved the file:

Press Win + R, type cmd, and hit Enter.

Use the cd command to go to your folder, e.g.:

cd C:\Users\YourName\Desktop


## Run the script:

python resourcemonitor.py

How It Works

The script checks your CPU and memory usage every 5 minutes.

If CPU > 80% or memory > 75%, it sends an email alert.

Alerts are sent only once every 12 hours to avoid spamming.

Every check is logged in:

server_monitor.log


You can open this file to see when your computer was busy.

## Tips

Keep your computer connected to the internet so the email alerts work.

You can change CPU and memory limits inside the script if you want different thresholds.

You can change the email address to send alerts to someone else.


This script helps you watch your computer like a superhero.
If your CPU or memory is too high, you get an email alert so you can take action!
