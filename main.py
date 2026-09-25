import dow

dow.makeCalendar(2026)

def getDayOfTheWeekForUserDate():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    day = int(input("Enter the day: "))
    print(dow.getDayOfTheWeek(year, month, day))

getDayOfTheWeekForUserDate()