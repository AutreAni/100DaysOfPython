import datetime as dt
from random import choice
import smtplib
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# credentials
sender_email = "ani.tests.it@gmail.com"
recipient_email = "ani.testsotherside@yahoo.com"
password = "fvri nggq rgls jshe"
def send_monday_quote(quote):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(from_addr=sender_email, to_addrs=recipient_email,
                            msg=f"Subject: Monday Motivation \n\n {quote}")
    print("email sent")

with open('quotes.txt', mode ="r", encoding="utf-8") as file:
    quotes_list = file.readlines()
    now = dt.datetime.now()
    if now.weekday() == 0:
        random_quote = choice(quotes_list).encode("ascii", "ignore").decode()
        send_monday_quote(random_quote)
