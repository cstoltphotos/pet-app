import smtplib
from email.message import EmailMessage

me = 'cstoltphotography@gmail.com'


with open('photoBookings.txt') as bookingFile:
    msg = EmailMessage()
    msg.set_content(bookingFile.read())
    bookingFile.readline()
    you = bookingFile.readline()
you = you.strip()
you = you.split(':')
you = you[-1].split

print(f"{you}")
msg['subject'] = 'New Photo Booing!'
msg['from'] = me
msg['to'] = you
