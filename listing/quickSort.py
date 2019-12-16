# Implementation of the quick sort algorithm.

# Sorts an array or list using the recursive quick sort algorithm.
def quickSort( theSeq ):
    n = len( theSeq )
    recQuickSort( theSeq, 0, n-1 )

# The recursive implementation using virtual segments.
def recQuickSort( theSeq, first, last ):
    # Check the base case.
    if first >= last :
        return
    else :
        # Save the pivot value.
        pivot = theSeq[first]

        # Partition the sequence and obtain the pivot position.
        pos = partitionSeq( theSeq, first, last )

        # Repeat the process on the two sub-sequences.
        recQuickSort( theSeq, first, pos - 1 )
        recQuickSort( theSeq, pos + 1, last )

# Partitions the subsequence using the first key as the pivot.
def partitionSeq( theSeq, first, last ):
    # Save a copy of the pivot value.
    pivot = theSeq[first]

    # Find the pivot position and move the elements around the pivot.
    left = first + 1
    right = last

    while left <= right :
        # Find the first key larger than the pivot.
        while left < right and theSeq[left] < pivot :
            left += 1

        # Find the last key in the sequence that is smaller than the pivot.
        while right >= left and theSeq[right] >= pivot :
            right -= 1

        # Swap the two keys if we have not completed this partition.
        if left < right :
            tmp = theSeq[left]
            theSeq[left] = theSeq[right]
            theSeq[right] = tmp

    # Put the pivot in the proper position.
    if right != first :
        theSeq[first] = theSeq[right]
        theSeq[right] = pivot

    # Return the index position of the pivot value.
    return right
