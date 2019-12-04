myBag = Bag()
myBag.add(19)
myBag.add(74)
myBag.add(23)
myBag.add(19)
myBag.add(12)

value = int(input("Guess a value contained in the bag."))
if vale in myBag:
    print("The bag contains the value", value)
else:
    print("the ban does not contains the value", value)
