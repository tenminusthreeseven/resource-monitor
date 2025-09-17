# resource-monitor


# Python Server Resource Monitor & Email Alert

This is a simple Python script that monitors your computer or server's CPU and memory usage.  
If usage exceeds set thresholds, it sends an email alert to notify you — helping you catch performance issues early.

---

## Features

- Checks CPU and memory usage every 5 minutes.
- Sends an email alert if CPU usage exceeds 80% or memory usage exceeds 75%.
- Limits alert emails to once every 12 hours to avoid spamming.
- Logs all resource checks and email alerts to a log file (`server_monitor.log`).
- Cross-platform: works on Linux, Windows, and macOS.

---

## Prerequisites

- Python 3.x installed on your system. Check by running:

  ```bash
  python3 --version
and then install by #pip install psutil

#points to note 
don't use normal password create by enabling 2 factor authorization and then add app password and you
will get password use by removing spaces and then run by python resourcemonitor.py 
