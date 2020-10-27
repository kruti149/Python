def isYearLeap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 != 0:
        return False
    elif year % 400 ==0:
       return True
    else:
        return False

def daysInMonth(year, month):
    if month == 2:
        leap = isYearLeap(year)
        # print ("leap yr is ", leap)
        if leap == True:
            return 29
        else:
            return 28;
    else:
        list = [1,3,5,7,8,10,12]
        if month in list:
            return 31
        else: 
            return 30

def dayOfYear(year, month, day):

    if isYearLeap(year):
        leapcount = 1
    else:
        leapcount = 2
    dayofyear = int((275 * month) / 9.0) - leapcount * int((month + 9) / 12.0) + day - 30
    return dayofyear


print(dayOfYear(2002, 6, 31))