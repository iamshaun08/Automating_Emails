import smtplib
from email.mime.text import MIMEText    #for message body
from email.mime.multipart import MIMEMultipart   #for from, to and subject
from email.mime.base import MIMEBase #for attachments
from email import encoders

sender = 'sender@outlook.com'
passw = 'your_password'
receiver = 'receiver@hotmail.com'

message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'Automating Emails!'

body = """
<h1>Hi John,</h1>

<p>This is an auto-generated email. PFA your Image!</p>

<h5>Regards</h5>
<h5>Jane</h5>
"""

mimetext = MIMEText(body, 'html')
message.attach(mimetext)

file_path = 'Files/image.jpg'
file = open(file_path, 'rb')
payload = MIMEBase('application', 'octate-stream')
payload.set_payload(file.read())
encoders.encode_base64(payload)
payload.add_header('Content-Disposition', 'attachment', filename=file_path)
message.attach(payload)

def html():
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login(sender, passw)
    server.sendmail(sender, receiver, message.as_string())
    server.quit()
    print("Email sent!")