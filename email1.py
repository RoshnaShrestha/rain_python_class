"""Generate or send the email"""

# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# sender_email = "roshhnnaashrestha@gmail.com"
# receiver_email = "ruman.metahorizon@gmail.com"
# password = "lvdw hufy cfba ppsd"

# #Create the email
# message = MIMEMultipart()
# message["From"] = sender_email
# message["To"] = receiver_email
# message["Subject"] = "Test Email"

# #Email Body 
# body = "Hello, the is a test email sent from Python."
# message.attach(MIMEText(body, "plain"))

# #Send the email
# try:
#     with smtplib.SMTP("smtp.gmail.com", 587) as server:
#         server.starttls()
#         server.login(sender_email, password)
#         server.sendmail (sender_email, receiver_email, message.as_string())
#     print("Email sent successfully!")
# except Exception as e:
#     print(f"Error: {e}")




"""Scheduled notification"""

import schedule
import time

def send_notification():
    print("This is your scheduled notification!")

#Schedule the notification every 10 seconds
schedule.every(10).seconds.do(send_notification)

print("Scheduler started. Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(1)