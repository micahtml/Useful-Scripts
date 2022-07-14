import smtplib

ReceiversList = ["abcd@gmail.com", "efgh@gmail.com", "hijk@gmail.com"]

for user in ReceiversList:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("YourEmailId@gmail.com", "YourEmailpassword")
    message = "I am spamming you with gmails hehe😅😅"
    s.sendmail("sender_email_id", user, message)
    s.quit()