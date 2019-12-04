from linearbag import Bag
from date import Date

def main():
    bornBefore = Date(6, 1, 1988)
    bag = Bag()

    date = promptAndExtractDate()
    while date is not None:
        print(date)
        bag.add(date)
        date = promptAndExtractDate()

    for date in bag:
        if date <= bornBefore:
            print("Is at least 21 years of age: ", date)
        else :
            print(date)

def promptAndExtractDate():
    print("Enter a birth date.")
    month = int(input("month (0 to quit): "))
    if month == 0:
        return None
    else:
        day = int(input("day: "))
        year = int(input("year: "))
        return Date(month, day, year)

main()
