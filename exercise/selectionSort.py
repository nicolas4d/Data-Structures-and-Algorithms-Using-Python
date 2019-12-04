def selectionSort(theSeq):
    n = len(theSeq)
    for i in range(n - 1):
        print(theSeq)
        smallNdx = i

        for j in range(i + 1, n):
            if theSeq[j] < theSeq[smallNdx]:
                smallNdx = j

        if smallNdx != i :
            tmp = theSeq[i]
            theSeq[i] = theSeq[smallNdx]
            theSeq[smallNdx] = tmp

theSeq = [80, 7, 24, 16, 43, 91, 35, 2, 19, 72]
selectionSort(theSeq)
print(theSeq)
