import smtplib
email_address = ""
password = ""

with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()
    connection.login(user=email_address, password=password)
    connection.sendmail(from_addr=email_address, to_addrs="hossien.arabnia@gmail.com", msg="My first email:Hello all pythoners!")