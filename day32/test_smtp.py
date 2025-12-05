import smtplib

with smtplib.SMTP("192.168.100.150") as connection:
    connection.sendmail(from_addr="root@raspberrypi", to_addrs="hossien.arabnia@gmail.com", msg="My first email:Hello all pythoners!")