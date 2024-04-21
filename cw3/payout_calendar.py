import calendar
import datetime

try:
    year = int(input("Enter a year: "))

    for month in range(1,12,1):
        last_day = calendar.monthrange(year, month)[1]
        last_weekday = calendar.weekday(year, month, last_day)
        last_friday = last_day - ((7 - (4 - last_weekday)) % 7)
        formatted_data = datetime.date(year, month, last_friday)
        print(calendar.month_name[month] + " " + str(formatted_data))

except:
    print("Input invalid")


