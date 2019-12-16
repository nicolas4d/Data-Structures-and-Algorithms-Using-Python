# Improved implementation of the merge sort algorithm.

from mergeVirtualSeq import mergeVirtualSeq

# Sorts a virtual subsequence in ascending order using merge sort.
def recMergeSort( theSeq, first, last, tmpArray ):
    # The elements that comprise the virtual subsequence are indicated
    # by the range [first...last]. tmpArray is temporary storage used in
    # the merging phase of the merge sort algorithm.

    # Check the base case: the virtual sequence contains a single item.
    if first == last :
        return;
    else :
    # Compute the mid point.
        mid = (first + last) // 2

    # Split the sequence and perform the recursive step.
    recMergeSort( theSeq, first, mid, tmpArray )
    recMergeSort( theSeq, mid+1, last, tmpArray )

    # Merge the two ordered subsequences.
    mergeVirtualSeq( theSeq, first, mid+1, last+1, tmpArray )
