from datetime import date

class Date:
    def __init__(self, month = 0, day = 0, year = 0):
        self._julianDay = 0

        if month == 0 :
            month = date.today().month
        if day == 0 :
            day = date.today().day
        if year == 0:
            year = date.today().year

        assert self._isValidGregorian(month, day, year), \
            "Invalid Gregorian date."
        tmp = 0
        if month < 3 :
            tmp = -1
        self._julianDay = day - 32075 + \
            (1461 * (year + 4800 + tmp) // 4) + \
            (367 * (month - 2 - tmp * 12) // 12) - \
            (3 * ((year + 4900 + tmp) // 100) // 4)

    def month(self):
        return (self._toGregorian())[0]

    def day(self):
        return (self._toGregorian())[1]

    def year(self):
        return (self._toGregorian())[2]

    def dayOfWeek( self ):
        month, day, year = self._toGregorian()
        if month < 3 :
            month = month + 12
            year = year - 1
        return ((13 * month + 3) // 5 + day + \
                year + year // 4 - year // 100 + year // 400) % 7

    def dayOfWeekName(self):
        week = self.dayOfWeek()
        if week == 0:
            return "Monday"
        elif week == 1:
            return "Tuesday"
        elif week == 2:
            return "Wednesday"
        elif week == 3:
            return "Thursday"
        elif week == 4:
            return "Friday"
        elif week == 5:
            return "Saturday"
        elif week == 6:
            return "Sunday"
        else:
            return None

    def __str__(self):
        month, day, year = self._toGregorian()
        return "%2d/%2d/%4d" % (month, day, year)

    def __eq__(self, otherDate):
        return self._julianDay == otherDate._julianDay

    def __lt__(self, otherDate):
        return self._julianDay < otherDate._julianDay

    def __le__(self, otherDate):
        return self._julianDay <= otherDate._julianDay

    def _toGregorian( self ):
        A = self._julianDay + 68569
        B = 4 * A // 146097
        A = A - (146097 * B + 3) // 4
        year = 4000 * (A + 1) // 1461001
        A = A - (1461 * year // 4) + 31
        month = 80 * A // 2447
        day = A - (2447 * month // 80)
        A = month // 11
        month = month + 2 - (12 * A)
        year = 100 * (B - 49) + year + A
        return month, day, year

    def monthName(self):
        month = self.month()
        if month == 1:
            return "January"
        elif month == 2:
            return "February"
        elif month == 3:
            return "March"
        elif month == 4:
            return "April"
        elif month == 5:
            return "May"
        elif month == 6:
            return "June"
        elif month == 7:
            return "July"
        elif month == 8:
            return "August"
        elif month == 9:
            return "September"
        elif month == 10:
            return "October"
        elif month == 11:
            return "November"
        elif month == 12:
            return "December"
        else:
            return "wrong month"

    def isLeapYear(self):
        return self._isLeapYear(self.year())

    def _isLeapYear(self, varYear):
        year = varYear

        if year % 4 == 0:
            if year % 100 != 0:
                return True

        if year % 100 == 0:
            if year % 400 == 0 :
                return True

        return False

    def julianDay(self):
        return self._julianDay

    def numDay(self, otherDate):
        numDay = self.julianDay() - otherDate.julianDay()

        if numDay < 0:
            numDay = 0 - numDay

        return numDay

    def advanceBy(self, days):
        assert type(days) == int, "Must be int variable"

        self._julianDay += days

        if self._julianDay < 0:
            self._julianDay = 0

    def _isValidGregorian(self, month, day, year):
        if month > 12 or month < 1:
            return False

        if month in [1,3,5,7,8,10,12]:
            if day > 31 or day < 1:
                return False

        elif month in [4,6,9,11]:
            if day < 1 or day > 30:
                return False

        elif month == 2:
            if self._isLeapYear(year):
                if day < 1 or day > 29:
                    return False
            else:
                if day < 1 or day > 28:
                    return False

        return True

    def dayOfYear(self):
        m = self.month()
        y = self.year()
        d = self.day()

        # 1, 2 month consider as 13, 14 month
        if m <= 2:
            m = m + 12
            d = d - 365
        # leap year one day
        elif m > 2 and self.isLeapYear():
            d = d + 1

        return int(30.6 * (m + 2 - 1)) - 63 + d

    def isWeekDay(self):
        week = self.dayOfWeek()

        if week == 5 or week == 6 :
            return True
        else:
            return False

    def isSpringEquinox(self):
        """whether is spring Equinox.

春分日期的计算 [Y*D+C]-L
公式解读：年数的后2位乘0.2422加20.646取整数减闰年数。21世纪春分的C值=20.646。
举例说明：2092年春分日期=[92×.0.2422+20.646]-[92/4]=42-23=19，3月19日是春分。
例外：2084年的计算结果加1日。
        """
        if self.month() != 3:
            return False

        y = self.year() % 100
        # return y
        d = 0.2422
        c = 20.646
        l = int(y/4)
        springEquinoxDay = int(y * d + c) - l

        if self.day() == springEquinoxDay:
            return True
        else:
            return False

    def isAutumnEquinox(self):
        """whether is autumn equinox.

秋分日期的计算 [Y*D+C]-L
公式解读：Y=年数后2位，D=0.2422，L=闰年数，21世纪C=23.042，20世纪=23.822。
举例说明：2088年秋分日期=[8×.0.2422+23.042]-[88/4]=44-22=22，9月22日是秋分。
例外：1942年的计算结果加1日。
        """

        if self.month() != 9:
            return False

        y = self.year() % 100
        d = 0.2422
        l = int(y/4)
        c = 23.042
        autumnEquinox = int(y*d+c) - l

        if self.day() == autumnEquinox:
            return True
        else:
            return False

    def isEquinox(self):
        """whether is equinox."""
        return self.isAutumnEquinox() or self.isSpringEquinox()

    def isSummerSolstice(self):
        """whether is summer solstice.

夏至日期的计算 [Y*D+C]-L
公式解读：Y=年数后2位，D=0.2422，L=闰年数，21世纪C=21.37，20世纪=22.20。
举例说明：2088年夏至日期=[88×.0.2422+21.37]-[88/4]=42-22=20，6月20日夏至。
例外：1928年的计算结果加1日。
        """

        if self.month() != 6:
            return False

        y = self.year() % 100
        d = 0.2422
        c = 21.37
        l = int(y/4)
        summerSolstice = int(y * d + c) - l

        if self.day() == summerSolstice:
            return True
        else:
            return False

    def isWinterSolstice(self):
        """whether is winter solstice.

冬至日期的计算 [Y*D+C]-L
公式解读：Y=年数后2位，D=0.2422，L=闰年数，21世纪C=21.94，20世纪=22.60。
举例说明：2088年冬至日期=[88×0.2422+21.94]-[88/4]=43-22=21，12月21日冬至。
例外：1918年和2021年的计算结果减1日。
        """
        if self.month() != 12:
            return False

        y = self.year() % 100
        d = 0.2422
        c = 21.94
        l = int(y / 4)
        winterSolstice = int(y * d + c) - l

        if self.day() == winterSolstice :
            return True
        else :
            return False

    def isSolstice(self):
        """whether is solstice."""
        return self.isSummerSolstice() or self.isWinterSolstice()

    def asGregorian(self, divchar = "/"):
        gregorian = self._toGregorian()
        month = gregorian[0]
        day = gregorian[1]
        year = gregorian[2]

        return str(month) + divchar + str(day) + divchar + str(year)

def printCalendar(date):
    month = date.month()
    day = date.day()
    year = date.year()

    if month in [1, 3, 5, 7, 8, 10, 12]:
        dayOfMonth = 31
    elif month in [4, 6, 9, 11]:
        dayOfMonth = 30
    elif month == 2:
        dayOfMonth = 28
        if date.isLeapYear():
            dayOfMonth += 1

    print()
    print("%12s %s" % (date.monthName(), year))
    print("%2s " * 7 % ("Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"))

    weekOfFirstDay = Date(month, 1, 2000).dayOfWeek()
    # print(date)
    # print(weekOfFirstDay)

    list = [" "] * 7
    countDay = 1
    for ndx in range(weekOfFirstDay, 7):
        list[ndx] = countDay
        countDay += 1

    printList(list)

    print()

    for curDay in range(countDay, dayOfMonth, 7):
        for curWeek in range(0, 7):
            if curDay <= dayOfMonth:
                list[curWeek] = curDay
                curDay += 1
            else:
                list[curWeek] = ""
        printList(list)
        print()

# sdfsfsdfdjsdf
def printList(list):
    for ndx in range(0, len(list)):
        print("%-2s " % list[ndx], end="")

