import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import json
import time

def sendMail(from_address, from_password, to_address, subject, content, server, port, attachmentName = ""):
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    body = MIMEText(content, 'plain')
    msg.attach(body)

    if (attachmentName != ""):
        filename= attachmentName
        with open(filename, 'r') as f:
            attachment = MIMEApplication(f.read(), Name=basename(filename))
            attachment['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filename))
        msg.attach(attachment)
        
    smtp = smtplib.SMTP(server, port)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(from_address, from_password)
    smtp.send_message(msg, from_address, to_address)
    smtp.close()

if __name__ == "__main__":
    to_addr = 'fimog58275@pamaweb.com'
    subject = 'Subject 1'
    content = 'Teste content'
    file = open('_secrets.json')
    secrets = json.load(file)
    while(True):
        print("Sending email")
        sendMail(secrets["username_email"], secrets["password_email"], to_addr, subject, content, secrets["server_email"], secrets["port_email_server"], "_testMail.txt")
        time.sleep(15)
    