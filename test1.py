import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('lahadenamh@gmail.com', 'dukegoogle2024')
server.sendmail('lahadenamh@gmail.com', '','Hello This is my first email from my email bot.')