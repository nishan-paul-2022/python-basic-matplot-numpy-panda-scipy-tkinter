import smtplib


fromemail = "nishan.paul.hello@gmail.com"
password = "hello007mlf1996"
smtpserver = "smtp.gmail.com:587"
toemail = "nishanpaul12011996se@gmail.com"
message = "hello world"
amount = 3

server = smtplib.SMTP(smtpserver)
server.starttls()
server.login(fromemail, password)
print(f"Sending {amount} emails")

for i in range(amount):
    server.sendmail(fromemail, toemail, message)
    print(i)

server.quit()
