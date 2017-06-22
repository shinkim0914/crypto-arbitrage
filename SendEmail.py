import smtplib

fromaddr = 'cryptoarbitrage2017@gmail.com'
toaddr = 'shinkim0914@gmail.com'

s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()
s.login('cryptoarbitrage2017@gmail.com', '6LiaMDnpQ72h')

msg = "\n Hello!"

s.sendmail(fromaddr,toaddr, msg)