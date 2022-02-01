"""
This case represents sending emails to multiple receivers. Change the sender and password before you test it!
"""

import yagmail
import pandas

def toContacts():
    sender = 'sender@gmail.com'
    passw = 'your_password'
    receiver = pandas.read_csv('CSV/contacts.csv')
    sub = "Automating Emails!"

    yag = yagmail.SMTP(user=sender, password=passw)

    for index, row in receiver.iterrows():
        body = [f"""
        Hi {row['name']}! This is an auto-generated email! PFA the text file!
        
        Regards
        Mike
        """, row['file']]
        yag.send(to=row['email'], subject=sub, contents=body)
    yag.close()
    print("Email(s) sent!")