import os
import smtplib

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login("lahadenamh@gmail.com", 'dukegoogle2024')

    subject = 'This is the subject'
    body = 'This is the body of the message'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail('lahadenamh@gmail.com', 'namh.lahade@duke.edu', msg)

print('Message is sent')