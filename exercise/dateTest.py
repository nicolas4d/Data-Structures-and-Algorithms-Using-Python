import unittest
from date import Date
from date import printCalendar

class TestDate(unittest.TestCase):
    def test__init__(self):
        "docstring"
        date = Date(0,0,0)
        print(date._toGregorian())
        date = Date(0, 1, 2000)
        print(date._toGregorian())
        date = Date(1, 0, 2000)
        print(date._toGregorian())
        date = Date(1, 1, 0)
        print(date._toGregorian())

        print("init test done")
        print()

    def test_monthName(self):
        date = Date(1, 1, 1990)
        self.assertEqual(date.monthName(), "January")
        date = Date(2, 1, 1990)
        self.assertEqual(date.monthName(), "February")
        date = Date(3, 1, 1990)
        self.assertEqual(date.monthName(), "March")
        date = Date(4, 1, 1990)
        self.assertEqual(date.monthName(), "April")
        date = Date(5, 1, 1990)
        self.assertEqual(date.monthName(), "May")
        date = Date(6, 1, 1990)
        self.assertEqual(date.monthName(), "June")
        date = Date(7, 1, 1990)
        self.assertEqual(date.monthName(), "July")
        date = Date(8, 1, 1990)
        self.assertEqual(date.monthName(), "August")
        date = Date(9, 1, 1990)
        self.assertEqual(date.monthName(), "September")
        date = Date(10, 1, 1990)
        self.assertEqual(date.monthName(), "October")
        date = Date(11, 1, 1990)
        self.assertEqual(date.monthName(), "November")
        date = Date(12, 1, 1990)
        self.assertEqual(date.monthName(), "December")

    def test_isLeapYear(self):
        # shiji runnian
        date = Date(1, 1, 2000)
        # print(2000 % 100)
        # print(2000 % 400)
        self.assertEqual(date.isLeapYear(), True)

        # putong runnian
        date = Date(1, 1, 2004)
        self.assertEqual(date.isLeapYear(), True)

        # bushi nunnian
        date = Date(1, 1, 2003)
        self.assertEqual(date.isLeapYear(), False)

        # teshu de bushi runnian
        date = Date(1, 1, 600)
        self.assertEqual(date.isLeapYear(), False)
        self.assertEqual(date._isLeapYear(2000), True)

    def test_julianDay(self) :
        date = Date(1, 1, 2000)
        # print(date.julianDay())
        self.assertEqual(date.julianDay(), 2451545)

    def test_numDay(self):
        date1 = Date(1, 1, 2000)
        date2 = Date(1, 2, 2000)
        # print(date1.julianDay())
        # print(date2.julianDay())
        self.assertEqual(date1.numDay(date2), 1)
        self.assertEqual(date2.numDay(date1), 1)

    def test_advanceBy(self):
        # date = Date(0, 0, 0)
        # date._julianDay = 0
        # print(date._toGregorian())

        # test plus
        date = Date(1, 1, 2000)
        julianDay = date.julianDay()
        date.advanceBy(1)
        newJulianDay = date.julianDay()
        self.assertEqual(julianDay + 1, newJulianDay)

        # test minus
        date = Date(1, 1, 2000)
        julianDay = date.julianDay()
        date.advanceBy(-1)
        newJulianDay = date.julianDay()
        self.assertEqual(julianDay - 1, newJulianDay)

        # test capped
        date = Date(1, 1, 2000)
        date.advanceBy(-999999999)
        self.assertEqual(date.julianDay(), 0)

    def test_isValidGregorian(self):
        date = Date(12, 1, 2000)
        self.assertEqual(date._isValidGregorian(333, 30, 2000), False)
        self.assertEqual(date._isValidGregorian(12, 1, 2000), True)
        self.assertEqual(date._isValidGregorian(2, 29, 2000 ), True)
        self.assertEqual(date._isValidGregorian(2, 30, 2000 ), False)

    def test_dayOfWeek(self):
        date = Date(1, 7, 2019)
        self.assertEqual(date.dayOfWeek(), 0)
        date = Date(1, 8, 2019)
        self.assertEqual(date.dayOfWeek(), 1)
        date = Date(1, 9, 2019)
        self.assertEqual(date.dayOfWeek(), 2)
        date = Date(1, 10, 2019)
        self.assertEqual(date.dayOfWeek(), 3)
        date = Date(1, 11, 2019)
        self.assertEqual(date.dayOfWeek(), 4)
        date = Date(1, 12, 2019)
        self.assertEqual(date.dayOfWeek(), 5)
        date = Date(1, 13, 2019)
        self.assertEqual(date.dayOfWeek(), 6)

        date = Date(12, 12, 2019)
        self.assertEqual(date.dayOfWeek(), 3)


    def test_dayOfWeekName(self):
        date = Date(1, 3, 2000)
        # print(date.dayOfWeekName())
        self.assertEqual(date.dayOfWeekName(), "Monday")
        date = Date(1, 4, 2000)
        self.assertEqual(date.dayOfWeekName(), "Tuesday")
        date = Date(1, 5, 2000)
        self.assertEqual(date.dayOfWeekName(), "Wednesday")
        date = Date(1, 6, 2000)
        self.assertEqual(date.dayOfWeekName(), "Thursday")
        date = Date(1, 7, 2000)
        self.assertEqual(date.dayOfWeekName(), "Friday")
        date = Date(1, 8, 2000)
        self.assertEqual(date.dayOfWeekName(), "Saturday")
        date = Date(1, 9, 2000)
        self.assertEqual(date.dayOfWeekName(), "Sunday")

    def test_month(self):
        date = Date(1, 1, 2000)
        # print(date.month())
        self.assertEqual(date.month(), 1)

    def test_dayOfYear(self):
        date = Date(1, 1, 2000)
        # print(date.dayOfYear())
        self.assertEqual(date.dayOfYear(), 1)
        date = Date(1, 31, 2000)
        self.assertEqual(date.dayOfYear(), 31)
        date = Date(2, 29, 2000)
        self.assertEqual(date.dayOfYear(), 31 + 29)
        date = Date(3, 1, 2000)
        self.assertEqual(date.dayOfYear(), 31 + 29 + 1)
        date = Date(12, 31, 2000)
        self.assertEqual(date.dayOfYear(), 366)

    def test_isWeekDay(self):
        date = Date(1, 1, 2000)
        self.assertEqual(date.isWeekDay(), True)
        date = Date(1, 2, 2000)
        self.assertEqual(date.isWeekDay(), True)
        date = Date(1, 3, 2000)
        self.assertEqual(date.isWeekDay(), False)

    def test_isSpringEquinox(self):
        date = Date(3, 21, 2019)
        # print(date.isSpringEquinox())
        self.assertEqual(date.isSpringEquinox(), True)
        date = Date(3, 20, 2019)
        self.assertEqual(date.isSpringEquinox(), False)
        date = Date(1, 20, 2019)
        self.assertEqual(date.isSpringEquinox(), False)

    def test_isAutumnEquinox(self):
        date = Date(9, 23, 2019)
        self.assertEqual(date.isAutumnEquinox(), True)
        date = Date(9, 21, 2019)
        self.assertEqual(date.isAutumnEquinox(), False)
        date = Date(3, 23, 2019)
        self.assertEqual(date.isAutumnEquinox(), False)

    def test_isEquinox(self):
        date = Date(9, 23, 2019)  # autumn equinox
        self.assertEqual(date.isEquinox(), True)
        date = Date(3, 21, 2019)  # spring equinox
        self.assertEqual(date.isEquinox(), True)
        date = Date(4, 4, 2019)
        self.assertEqual(date.isEquinox(), False)

    def test_isSummerSolstice(self):
        date = Date(6, 21, 2019)
        self.assertEqual(date.isSummerSolstice(), True)
        date = Date(5, 21, 2019)
        self.assertEqual(date.isSummerSolstice(), False)
        date = Date(6, 22, 2019)
        self.assertEqual(date.isSummerSolstice(), False)

    def test_isWinterSolstice(self):
        date = Date(12, 22, 2019)
        self.assertEqual(date.isWinterSolstice(), True)
        date = Date(1, 22, 2019)
        self.assertEqual(date.isWinterSolstice(), False)
        date = Date(12, 23, 2019)
        self.assertEqual(date.isWinterSolstice(), False)

    def test_isSolstice(self):
        date = Date(6, 21, 2019)
        self.assertEqual(date.isSummerSolstice(), True)
        date = Date(5, 21, 2019)
        self.assertEqual(date.isSummerSolstice(), False)
        date = Date(6, 22, 2019)
        self.assertEqual(date.isSummerSolstice(), False)
        date = Date(12, 22, 2019)
        self.assertEqual(date.isWinterSolstice(), True)
        date = Date(1, 22, 2019)
        self.assertEqual(date.isWinterSolstice(), False)
        date = Date(12, 23, 2019)
        self.assertEqual(date.isWinterSolstice(), False)

    def test_asGregorian(self):
        date = Date(12, 12, 2019)
        # print(date.asGregorian())
        self.assertEqual(date.asGregorian(), "12/12/2019")
        self.assertEqual(date.asGregorian(","), "12,12,2019")

# sdfs
class functionTest(unittest.TestCase):
    def test_printCalendar(TestCase):
        date = Date(12,12,2019)
        printCalendar(date)
        date = Date(11,1,2019)
        printCalendar(date)

unittest.main()
