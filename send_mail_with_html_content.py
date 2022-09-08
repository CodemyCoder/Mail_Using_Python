# Importing modules
import os
import ssl as secureSSL
from email.message import EmailMessage
import smtplib

# Do remember to create environment variables for your EmailId and Password
User = os.getenv("Gmail_User") # Fetched from environment variables 
Pass = os.getenv("Gmail_Pass") # Fetched from environment variables 
# dataFile = open("./project.html", "r").read() # Can be any html file you created but not with advanced logic or methods.
msg = EmailMessage()
msg["From"] = User
msg["To"] = User # Here it can have all the email-id list whom you want to send the mail.
msg["Subject"] = "Python Mail App Test Port 465" # Subject for your mail
# msg.set_content("<h1>lorem is a dummy para by VsCode Part 2</h1>", subtype="html") # This Is used to set the mail body ( can be html or normal text nothing matters here) but it's subtype should be html
fileData = open("./project.html", "r").read() # Can be any html file you created but not with advanced logic or methods.
# msg.add_header("Content-Type", "text/html") # used to set the type and subtype of mail body when using set_payload() method
# msg.set_payload(fileData) # another method like set_content()
msg.set_content(fileData, subtype="html") # created mail body content by reading data from a HTML file.

# Logic for send the mail safely.

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
    smtp.login(User, Pass) # Used to create a secure connection between the mail server and the account owner.
    smtp.send_message(msg) # Used to send all the content of the mail (i.e, subject, body, files or attachments)
