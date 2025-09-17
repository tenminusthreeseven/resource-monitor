import psutil
import smtplib
import logging
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ====== CONFIG SETTINGS ======
CPU_THRESHOLD = 80     # percent
MEMORY_THRESHOLD = 75  # percent
CHECK_INTERVAL = 300   # seconds = 5 minutes
EMAIL_COOLDOWN = 43200 # seconds = 12 hours

EMAIL_FROM = "your_email@gmail.com"
EMAIL_TO = "recipient_email@example.com"
EMAIL_PASSWORD = "your_app_password"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

LOG_FILE = "server_monitor.log"

# ====== LOGGING SETUP ======
logging.basicConfig(filename=LOG_FILE,
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# ====== FUNCTION: Send Email ======
def send_email(subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_FROM
        msg['To'] = EMAIL_TO
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        logging.info("Email alert sent.")
    except Exception as e:
        logging.error(f"Email failed: {e}")

# ====== FUNCTION: Check System Health ======
def check_system_resources(last_alert_time):
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    logging.info(f"CPU: {cpu}%, Memory: {memory}%")

    current_time = time.time()
    if (cpu > CPU_THRESHOLD or memory > MEMORY_THRESHOLD) and (current_time - last_alert_time > EMAIL_COOLDOWN):
        subject = "Server Alert: High Resource Usage"
        body = (f"⚠️ High resource usage detected!\n\n"
                f"CPU Usage: {cpu}% (Limit: {CPU_THRESHOLD}%)\n"
                f"Memory Usage: {memory}% (Limit: {MEMORY_THRESHOLD}%)")
        send_email(subject, body)
        return current_time  # Update last alert time
    return last_alert_time  # No update

# ====== MAIN LOOP ======
if __name__ == "__main__":
    logging.info("Monitoring started.")
    last_email_sent = 0  # Timestamp of last email

    while True:
        last_email_sent = check_system_resources(last_email_sent)
        time.sleep(CHECK_INTERVAL)
