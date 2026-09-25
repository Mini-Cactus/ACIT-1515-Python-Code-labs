def getDayOfTheWeek(year, month, day):
    dotw_list = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    offset_list = [6,4,2,-1]
    month_code = [1,4,4,0,2,5,0,3,6,1,4,6]

    twelves = int(str(year)[2:]) // 12
    remainder = int(str(year)[2:]) % 12
    fours = remainder // 4
    monthcode = month_code[month - 1]
    if isLeapYear(year) == True and month <= 2:
        offset1 = offset_list[3]
    else:
        offset1 = 0
    if 1600 <= year <= 1699 or 2000 <= year <= 2099:
        offset2 = offset_list[0]
    elif 1700 <= year <= 1799 or 2100 <= year <= 2199:
        offset2 = offset_list[1]
    elif 1800 <= year <= 1899:
        offset2 = offset_list[2]
    else:
        offset2 = 0
    dotw = (twelves + remainder + fours + monthcode + day + offset1 + offset2) % 7
    dotw = dotw_list[dotw]
    return f"{day}-{month}-{year} is a {dotw}"

def isLeapYear(year):
    if year == 1700 or year == 1800 or year == 1900 or year == 2100 or year == 2200 or year == 2300:
        return False
    
    if year % 4 == 0:
        return True
    else:
        return False
    
def makeCalendar(year):
    jan = 31
    feb = 28
    mar = 31
    apr = 30
    may = 31
    jun = 30
    jul = 31
    aug = 31
    sep = 30
    octo = 31
    nov = 30
    dec = 31
    monthdays = [jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec]

    for month in range(len(monthdays)):
        for day in range(monthdays[month]):
            print(getDayOfTheWeek(year, month + 1, day + 1))