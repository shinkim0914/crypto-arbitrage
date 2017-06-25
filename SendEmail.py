import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send(text):
    fromaddr = 'cryptoarbitrage2017@gmail.com'
    toaddr = ['shinkim0914@gmail.com', 'honki91@gmail.com', 'snowjoon@gmail.com']

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['Subject'] = "Spread threshold has been exceeded"
    msg_body = MIMEText(text, 'plain')
    msg.attach(msg_body)

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login('cryptoarbitrage2017@gmail.com', '6LiaMDnpQ72h')

    for addr in toaddr:
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['Subject'] = "Spread threshold has been exceeded"
        msg['To'] = addr
        msg_body = MIMEText(text, 'plain')
        msg.attach(msg_body)
        s.send_message(msg)