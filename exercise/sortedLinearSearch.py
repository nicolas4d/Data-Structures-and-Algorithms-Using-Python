def sortedLinearSearch(theValues, target):
    n = len(theValues)
    for i in range(n):
        if theValues[i] == target:
            return True
        elif theValues[i] < target:
            return False
    return False

theValues = [1, 2, 4, 5]
target = 1
print(sortedLinearSearch(theValues, target))

target = 9
print(sortedLinearSearch(theValues, target))
