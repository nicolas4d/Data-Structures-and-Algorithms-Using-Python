def insertionSort(theSeq):
    n = len(theSeq)
    for i in range(1, n):
        print(theSeq)
        value = theSeq[i]
        pos = i
        while pos > 0 and value < theSeq[pos - 1] :
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1

        theSeq[pos] = value

seq = [80, 7, 24, 16, 43, 91, 35, 2, 19, 72]
insertionSort(seq)
print(seq)
