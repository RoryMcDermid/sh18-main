import datetime


date = (datetime.datetime.today() - datetime.timedelta(days=1))
formatted_date = str(date.day) + "/" + str(date.month) + "/" + str(date.year)
print(formatted_date)
    
    