import os
import ssl as secureSSL
from email.message import EmailMessage
import smtplib

User = os.getenv("Gmail_User")
Pass = os.getenv("Gmail_Pass")
dataFile = open("project.html", "r").read()
msg = EmailMessage()
msg["From"] = User
msg["To"] = User
msg["Subject"] = "Python Mail App Test Port 465"
# msg.set_content("<h1>lorem is a dummy para by VsCode Part 2</h1>", subtype="html")
fileData = open("./project.html", "r").read()
# msg.add_header("Content-Type", "text/html")
# msg.set_payload(fileData)
msg.set_content(fileData, subtype="html")

# print("User", User)
# with smtplib.SMTP("localhost", "8888") as smtp:
#     smtp.send_message(msg)
context = secureSSL.create_default_context()
# with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
#     smtp.ehlo()
#     smtp.starttls(context=context)
#     smtp.ehlo()
#     smtp.login(User, Pass)
#     smtp.send_message(msg)

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(User, Pass)
    smtp.send_message(msg)
