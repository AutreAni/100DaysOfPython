##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
from random import  randint
import smtplib

#get current day and month
now = dt.datetime.now()
today = now.day
this_month = now.month

birthdays = pandas.read_csv("birthdays.csv")
# gmail credentials
sender_email = "ani.tests.it@gmail.com"
password = "fvri nggq rgls jshe"
def send_birthday_email(recipient):
    with open(f"letter_templates/letter_{randint(1,3)}.txt", mode = "r") as letter_file:
        letter = letter_file.read()
        letter = letter.replace("[NAME]", recipient["name"]).replace("Angela", "Ani")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=sender_email, password=password)
            connection.sendmail(from_addr = sender_email, to_addrs=recipient["email"], msg = f"Subject: Happy Birthday!!!\n\n{letter}" )



for (index, row) in birthdays.iterrows():
    day = row["day"]
    month = row["month"]
    email = row["email"]
    name = row["name"]
    if day == today and month == this_month:
        send_birthday_email({"email":email, "name": name})



