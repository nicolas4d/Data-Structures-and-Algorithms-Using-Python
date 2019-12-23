# A simple implementation of the heapsort algorithm.

def simpleHeapSort( theSeq ):
    # Create an array-based max-heap.
    n = len(theSeq)
    heap = MaxHeap( n )

    # Build a max-heap from the list of values.
    for item in theSeq :
        heap.add( item )

    # Extract each value from the heap and store them back into the list.
    for i in range( n, 0, -1 ) :
        theSeq[i] = heap.extract()
