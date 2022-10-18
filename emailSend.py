import smtplib, ssl
import random
from email.message import EmailMessage

def mailing(reciever,subject,text):
        gmail_user = 'softdev2568@gmail.com'
        gmail_pwd = 'softdev.tk'
        message = EmailMessage()
        message.set_content(text)
        message['Subject'] = subject
        message['To'] = reciever
        message['From'] = gmail_user

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gmail_user, gmail_pwd)

        server.send_message(message)
        server.quit()
        return 'success'