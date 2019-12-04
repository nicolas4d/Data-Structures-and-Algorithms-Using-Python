def findSmallest(theValues):
    n = len(theValues)
    smallest = theValues[0]
    for i in range(1, n):
        if smallest > theValues[i]:
            smallest = theValues[i]
    return smallest

theValues = [1, 2, 4, 5, 6, 7, 8, 9, 10]
print(findSmallest(theValues))

