
# This function checks if year is a leap year.
# It is wrong: 1900 was a common year!
def isLeapYear(year):
    if year%4 == 0 and not year%100 == 0:
        return 0==0
    elif year%400==0 :
        return 0==0
    else:
        return 0==1


def monthDays(year, month):
    if isLeapYear(year) == 0 :
        MONTHDAYS = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        days = MONTHDAYS[month]
        return days
    else:
        MONTHDAYS = (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        days = MONTHDAYS[month]
        return days


def nextDay(year, month, day):
    if monthDays(year, month)==28:
        if day < 28:
            day += 1
        elif day == 28:
            day = 1
            month += 1
    elif monthDays(year,month)==29:
        if day < 29 :
            day += 1
        elif day == 29:
            day = 1
            month += 1
    elif monthDays(year,month)==30:
        if day < 30:
            day += 1
        elif day == 30:
            day = 1
            month += 1
    else:
        if day < 31 :
            day += 1
        elif day == 31:
            if month == 12:
                day = 1
                month = 1
                year += 1
            else:
                day = 1
                month += 1
    return year, month, day

def main():
    print("Was", 2017, "a leap year?", isLeapYear(2017))    # False?
    print("Was", 2016, "a leap year?", isLeapYear(2016))    # True?
    print("Was", 2000, "a leap year?", isLeapYear(2000))    # True?
    print("Was", 1900, "a leap year?", isLeapYear(1900))    # False?
    
    print("January 2017 had", monthDays(2017, 1), "days")   # 31?
    print("February 2017 had", monthDays(2017, 2), "days")  # 28?
    print("February 2016 had", monthDays(2016, 2), "days")  # 29?
    print("February 2000 had", monthDays(2000, 2), "days")  # 29?
    print("February 1900 had", monthDays(1900, 2), "days")  # 28?
    
    y, m, d = nextDay(2017, 1, 30)
    print(y, m, d)    # 2017 1 31 ?
    y, m, d = nextDay(2017, 1, 31)
    print(y, m, d)    # 2017 2 1 ?
    y, m, d = nextDay(2017, 2, 28)
    print(y, m, d)    # 2017 3 1 ?
    y, m, d = nextDay(2016, 2, 29)
    print(y, m, d)    # 2016 3 1 ?
    y, m, d = nextDay(2017, 12, 31)
    print(y, m, d)    # 2018 1 1 ?

# call the main function
main()
