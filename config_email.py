import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def pombo(email_sender, senha, email_receiver, groupo):
    for i in email_receiver:
        message = MIMEMultipart()
