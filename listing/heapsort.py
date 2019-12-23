# Improved implementation of the heapsort algorithm.

# Sorts a sequence in ascending order using the heapsort.
def heapsort( theSeq ):
    n = len(theSeq)

    # Build a max-heap within the same array.
    for i in range( n ) :
        siftUp( theSeq, i )

    # Extract each value and rebuild the heap.
    for j in range( n-1, 0, -1) :
        tmp = theSeq[j]
        theSeq[j] = theSeq[0]
        theSeq[0] = tmp
        siftDown( theSeq, j-1, 0 )
