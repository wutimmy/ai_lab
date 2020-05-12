import smtplib, ssl
port = 587  # For starttls
smtp_server = "smtp.gmail.com"

def send_mail(sender_email="codeme2006@gmail.com", receiver_email=str, message=""):
    try:
        password = "Wulokhin2006"
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    except:
        pass

send_mail("wu@gmail.com", message="")
