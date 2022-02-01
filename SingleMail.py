"""
This case represents sending a single mail to a single receiver. Change the sender email and password before you use it!
"""

import yagmail

def singleMail():
  sender = 'sender@gmail.com'
  receiver = input("Enter receiver mail: ")
  sub = input("Enter subject: ")
  body = input("Enter body: ")
  passw = 'your_password'
  yag = yagmail.SMTP(user = sender, password = passw)
  yag.send(to=receiver, subject=sub, contents=body)
  print("Email sent!")
  yag.close()