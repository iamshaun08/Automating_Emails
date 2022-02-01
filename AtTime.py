"""
This case represents sending a single mail to the receiver at a particular time of the day.
Change the sender, receiver and password before you test it!
"""

import yagmail  #to log in to your gmail and send
import time
from datetime import datetime as dt


sender = 'sender@gmail.com'
receiver = 'receiver@gmail.com'
sub = 'Automating Mails!'
body = 'This is an auto-generated email!'
passw = 'your_password'
yag = yagmail.SMTP(user = sender, password = passw)
h = 20
m = 30

def atTime():
  while True:
    now = dt.now()
    if now.hour == h and now.minute == m:
        yag.send(to=receiver, subject=sub, contents=body)
        print("Email sent!")
        time.sleep(60)

yag.close()