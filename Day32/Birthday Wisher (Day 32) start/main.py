import smtplib
import datetime as dt
import random

my_email = "test@email.com"
password = "teste"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open("quotes.txt") as quotes_files:
        all_quotes = quotes_files.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("outlook.office365.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="test@email.com",
            msg=f"Subject:Monday Motivational Quotes\n\n{quote}"
        )












#import smtplib

#my_email = "viniciusmotero@hotmail.com"
#password = "casa68"

#with smtplib.SMTP("outlook.office365.com") as connection:
#    connection.starttls()
#    connection.login(user=my_email, password=password)
#    connection.sendmail(
#        from_addr=my_email,
#        to_addrs="mouradeoterovinicius@gmail.com",
#        msg="Subject:Hello\n\nThis is the body of my email."
#    )



#import datetime as dt


#now = dt.datetime.now()
#year = now.year
#month = now.month
#day = now.day

#date_of_bith = dt.datetime(year=1998, month=9, day=16)
#year_old= year-date_of_bith.year
#print(year_old)


