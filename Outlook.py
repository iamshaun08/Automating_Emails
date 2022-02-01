"""
This case represents sending an email from your outlook account.
Change the sender, receiver and password before you test it!
"""

import smtplib

sender = 'sender@outlook.com'
passw = 'your_password'
receiver = 'receiver@hotmail.com'

body = """\
Subject: Automating emails!

This is an auto-generated email.
Regards
Mike
"""
def outlook():
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login(sender, passw)
    server.sendmail(sender, receiver, body)
    server.quit()
    print("Email sent!")