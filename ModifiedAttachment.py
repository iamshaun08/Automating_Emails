"""
This case represents sending emails to multiple receivers with modified and personalized attachments.
Change the sender and password before you test it!
"""

import pandas   #ro read csv
import yagmail

def modifiedAttachment():
    sender = 'sender@gmail.com'
    passw = 'your_password'

    yag = yagmail.SMTP(user=sender, password=passw)
    codes = pandas.read_csv('CSV/codes.csv')
    sub = 'Your recovery code!'

    for index,row in codes.iterrows():
        name = row['name']
        code = row['code']
        receiver = row['email']

        generate_txt(name, code)
        file = f'Files/{name}.txt'
        body = [f"""
        Greetings {name}!
        PFA your recovery code in the .txt file!
        
        Note: This is an auto-generated email. Do not reply!
        Regards
        Mike
        """, file]

        yag.send(to=receiver, subject=sub, contents=body)
    yag.close()
    print("Emails sent!")


def generate_txt(name, code):
    with open(f'Files/{name}.txt', 'w') as file:
        file.write(f"""Your code is {str(code)}. Keep it secure!
        """)