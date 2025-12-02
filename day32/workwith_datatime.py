import datetime as dt

from dateutil.rrule import weekday

time = dt.datetime.now()

print(time.year)
print(time.month)
print(time.day)
print(time.hour)
print(time.minute)
print(time.second)
print(time.weekday())

my_birthday = dt.datetime(1998, 1, 21, 11, 20)
print(my_birthday.weekday())