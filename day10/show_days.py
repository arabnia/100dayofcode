# this app show you every month has how many days in it

def leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False

def day_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if not leap_year(year=year):
        print(month_days[month])
    elif leap_year(year=year):
        month_days[1] = 29
        print(month_days[month])

day_in_month(int(  input("what's year? ")  ), int(  input("what's mount? ")  ) -1    )
