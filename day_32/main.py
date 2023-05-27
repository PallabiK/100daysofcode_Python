import datetime as dt
import smtplib
import random

now = dt.datetime.now()
day_of_the_week = now.weekday()

my_email = "your_email@gmail.com"
password = "your_password"
receiver_email = "recipient_email@anything.com"

with open("quotes.txt") as data:
    quotes = data.readlines()

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    if day_of_the_week == 5:
        connection.sendmail(from_addr=my_email,
                            to_addrs=receiver_email,
                            msg=f"Subject:Day32\n\n{random.choice(quotes)}")



date_of_birth = dt.datetime(year=1993, month=7, day=7, hour=4)
print(date_of_birth)

