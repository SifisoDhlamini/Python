# yprosgqhbanezonn

from email.message import EmailMessage
from config import password
import ssl
import smtplib


email_sender = "sifisodhlamini83@gmail.com"
email_password = password()

email_receiver = "pekevit676@galotv.com"

subject = "From Scifi_the_dev"

body ="""
This a message from Scifi_the_dev sent via a Python script.

Kind regards,
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(email_sender, email_password)
    server.send_message(em)
    print("Email sent!")
    server.quit()

# with smtplib.SMTP_SSL("smpt.gmail.com", 465, context=context) as smtp:
#     smtp.login(email_sender, email_password)
#     smtp.sendmail(email_sender, email_receiver, em.as_string())

