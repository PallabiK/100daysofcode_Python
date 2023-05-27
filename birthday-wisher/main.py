##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib

my_email = "your_email@gmail.com"
password = "your_password"

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today = (now.month, now.day)

birthdays = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in birthdays.iterrows()}


if today in birthdays_dict:
    number = random.randint(1, 3)
    print(number)
    with open(f"letter_templates/letter_{number}.txt") as letter_file:
        letter_content = letter_file.read()
        new_letter = letter_content.replace("[NAME]", birthdays_dict[today]["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthdays_dict[today]["email"],
                            msg=f"Subject:HAPPY BIRTHDAY\n\n{new_letter}")








