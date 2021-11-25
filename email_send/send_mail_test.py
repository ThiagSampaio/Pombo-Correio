import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(email, senha, lista_email, titulo_email, texto_email):
    lista_email_erro = []
    print(f'Estou na lista:{lista_email}')

    for item in lista_email:
        sender_address = email
        sender_pass = senha
        receiver_address = item

        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = titulo_email
        message.attach(MIMEText(texto_email, 'html'))
        # Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()  # eHabilita segurança

        print(f'Estou no email{item}')
        try:
            session.login(sender_address, sender_pass)

        except smtplib.SMTPAuthenticationError:
            session.quit()
            pass
            # return (False, "Erro no email ou senha")

        try:
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
            pass
            # return (True, "Tudo OK")

        except smtplib.SMTPRecipientsRefused:
            print('estou no erro')
            lista_email_erro.append(item)
            session.quit()
            return (lista_email_erro)


def send_mail_test1(email, senha):

    sender_address = email
    sender_pass = senha
    receiver_address = email

    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = "Teste plataforma"
    message.attach(
        MIMEText('Este é um email para teste do pombo correio', 'plain'))

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
