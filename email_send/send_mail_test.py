import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(email, senha):
    testText = "Essa é uma msg de teste da plataforma pombo-correio"

    sender_address = email
    sender_pass = senha
    receiver_address = email

    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Teste de email mandado pelo pombo-correio.'
    message.attach(MIMEText(testText, 'plain'))
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()  # eHabilita segurança
    try:
        session.login(sender_address, sender_pass)

    except smtplib.SMTPAuthenticationError:
        session.quit()
        return (False, "Erro no email ou senha")

    try:
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        return (True, "Tudo OK")

    except smtplib.SMTPRecipientsRefused:
        return (False, "Não pode enviar para esse email")
