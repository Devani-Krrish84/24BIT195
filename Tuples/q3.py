date1 = (17, 9, 2006)
date2 = (5, 7, 2007)

def count_no_days(date1, date2) :
    days = 0
    months = 0
    years = 0

    months += 12 - date1[1] + date2[1]
    days += 31 - date1[0] + date2[0]
    years += date2[2] - date1[2]

    return days + months * 30 + years * 365

days = count_no_days(date1, date2)
print("Total number of days between", date1, "and", date2, "is", days)