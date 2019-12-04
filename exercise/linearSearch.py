def linearSearch(theValues, target):
    n = len(theValues)
    for i in range(n):
        if theValues[i] == target:
            return True
    return False

theValues = [1, 2]
target = 1
print(linearSearch(theValues, target))
target = 2
print(linearSearch(theValues, target))
target = 3
print(linearSearch(theValues, target))

