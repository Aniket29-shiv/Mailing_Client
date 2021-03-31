import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP(''smtp.gmail.com', 25')

server.ehlo()

with open('pass.txt','r') as f:
    password = f.read()


server.login('<name>@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = '<name>@gmail.com'
msg['To'] = '<name2>@gmail.com'
msg['Subject'] = 'Just A Test... Hello!'

with open('message.txt','r') as f:
    message = f.read

msg.attach(MIMEText(message,'plain'))

filename = '1.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application','octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachment; filename={filename}')

text = msg.as_string()
server.sendmail('<name>@gmail.com','<name2>@gmail.com', text)