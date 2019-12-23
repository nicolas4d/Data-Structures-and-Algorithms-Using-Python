from arrayheap import MaxHeap

# A simple implementation of the heapsort algorithm.
def simpleHeapSort(theSeq):
    # create an array-based max-heap.
    n = len(theSeq)
    heap = MaxHeap(n)

    # Build a max-heap from the list of values.
    for item in theSeq :
        heap.add(item)

    for item in heap._elements:
        print(item, end=" ")

    print()

    # Extract each value from the heap and store them back into the list.
    for i in range(n - 1 , -1, -1):
        theSeq[i] =  heap.extract()
        print(theSeq[i])

        for item in heap._elements:
            print(item, end=" ")

        print()


