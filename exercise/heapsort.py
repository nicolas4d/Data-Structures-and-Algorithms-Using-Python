# Improved implementation of the heapsort algorithm.

# Sorts a sequence in ascending order using the heapsort.
def heapsort(theSeq):
    n = len(theSeq)

    # Build a max-heap within the same array.
    for i in range(n):
        siftUp(theSeq, i)

    # Extract each value and rebuild the heap.
    for j in range(n - 1, 0, -1):
        tmp = theSeq[j]
        theSeq[j] = theSeq[0]
        theSeq[0] = tmp

        siftDown(theSeq, j, 0)

# Sift the value at the ndx element up the tree.
def siftUp(theSeq, ndx):
    if ndx > 0:
        parent = ndx // 2

        # swap elements
        if theSeq[ndx] > theSeq[parent]:
            tmp = theSeq[ndx]
            theSeq[ndx] = theSeq[parent]
            theSeq[parent] = tmp
            siftUp(theSeq, parent)

# Sift the value at the ndx element down the tree.
def siftDown(theSeq, count, ndx):
    left = 2 * ndx + 1
    right = 2 * ndx + 2

    # Determine which node contains the larger value.
    largest = ndx

    if left < count and \
       theSeq[left] >= theSeq[largest]:
        largest = left
    if right < count and \
       theSeq[right] >= theSeq[largest]:
        largest = right

    # If the largest value is not in the current node (ndx), swap it with
    # the largest value and repeat the process.
    if largest != ndx:
        # swap(theSeq[ndx], theSeq[largest])
        tmp = theSeq[ndx]
        theSeq[ndx] = theSeq[largest]
        theSeq[largest] = tmp

        siftDown(theSeq, count, largest)

theSeq = [9, 3, 2, 5, 4]
heapsort(theSeq)
print(theSeq)
