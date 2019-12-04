def bubbleSort(theSeq):
    n = len(theSeq)
    for i in range(n - 1):
        print(theSeq)
        for j in range(n - 1 - i):
            if theSeq[j] > theSeq[j + 1]:
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp

theSeq = [80, 7, 24, 16, 43, 91, 35, 2, 19, 72]
bubbleSort(theSeq)
print(theSeq)

# enhance version
def bubbleSort_enhance(theSeq):
    n = len(theSeq)
    for i in range(n - 1):
        swapped = 0

        for j in range(n - 1 - i):
            if theSeq[j] > theSeq[j + 1]:
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
                swapped += 1

        if swapped == 0:
            print("don't needed to sort again!")
            return

