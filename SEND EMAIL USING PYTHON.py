from decimal import Context
import smtplib
import ssl
from email.message import EmailMessage

subject="blalalala"
body="aaaa"
sender_email="balalalal@gmail.com"
receiver_email="balalalal@gmail.com"
password = input("enter a password: ")

message = EmailMessage()
message["from"] = sender_email
message["to"] = receiver_email
message["subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("sending email")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, Context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string)

print("success")