def findAllNeg(values):
    negList = list()

    for elem in values:
        if elem < 0:
            negList.append(elem)

    return negList

values = [1, 2, 3, 4, 5, -1, -2, -4, -7]
print(findAllNeg(values))
