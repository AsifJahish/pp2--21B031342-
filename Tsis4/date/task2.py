
import datetime


def today_yesterday_tomorrow_date():

    yesterdayDate= datetime.date.today()- datetime.timedelta(days=1)
    tomorrowDate= datetime.date.today()+ datetime.timedelta(days=1)

    return F"today date is {datetime.date.today()} \n, the yesterday date was: {yesterdayDate} \n and the tomorrow will be : {tomorrowDate}"

a= today_yesterday_tomorrow_date()
print(a)
    