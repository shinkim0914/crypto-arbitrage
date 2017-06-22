import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send(text):
    fromaddr = 'cryptoarbitrage2017@gmail.com'
    toaddr = 'shinkim0914@gmail.com'

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Spread threshold has been exceeded"
    msg_body = MIMEText(text, 'plain')
    msg.attach(msg_body)

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login('cryptoarbitrage2017@gmail.com', '6LiaMDnpQ72h')
    s.send_message(msg)