import smtplib
from email.message import EmailMessage

sender_email = "email@uj.edu.pl"
receiver = "XXXX"

password = input("Enter password:")

with open("text.txt", "r") as text:
    content = text.read()

msg = EmailMessage()
msg["Subject"] = "Test"
msg.set_content(content)

serwer_smtp = smtplib.SMTP("smtp.office365.com", 587)
serwer_smtp.starttls()
serwer_smtp.login(sender_email, password)

serwer_smtp.send_message(msg, from_addr=sender_email, to_addrs=receiver)

serwer_smtp.quit()

print("Send")




