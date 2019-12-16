# Merging two ordered virtual sublists.

# Merges the two sorted virtual subsequences: [left..right) [right..end)
# using the tmpArray for intermediate storage.
def mergeVirtualSeq( theSeq, left, right, end, tmpArray ):
    # Initialize two subsequence index variables.
    a = left
    b = right

    # Initialize an index variable for the resulting merged array.
    m = 0

    # Merge the two sequences together until one is empty.
    while a < right and b < end :
        if theSeq[a] < theSeq[b] :
            tmpArray[m] = theSeq[a]
            a += 1
        else :
            tmpArray[m] = theSeq[b]
            b += 1
            m += 1

    # If the left subsequence contains more items append them to tmpArray.
    while a < right :
        tmpArray[m] = theSeq[a]
        a += 1
        m += 1

    # Or if right subsequence contains more, append them to tmpArray.
    while b < end :
        tmpArray[m] = theSeq[b]
        b += 1
        m += 1

    # Copy the sorted subsequence back into the original sequence structure.
    for i in range( end - left ) :
        theSeq[i+left] = tmpArray[i]
