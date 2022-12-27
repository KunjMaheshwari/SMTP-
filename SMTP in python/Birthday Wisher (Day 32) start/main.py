import smtplib
import random
import datetime as dt

my_email = "kunj1766@gmail.com"
password = "xpbnblocqdlhxyvn"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:   # 0 means Monday
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="kunj.maheshwari2021@vitbhopal.ac.in",
                            msg=f"Subject:Wednesday Motivation\n\n{quote}")
