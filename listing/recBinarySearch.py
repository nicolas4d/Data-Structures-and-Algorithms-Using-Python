# Performs a recursive binary search on a sorted sequence.
def recBinarySearch( target, theSeq, first, last ):
    # If the sequence cannot be subdivided further, we are done.
    if first > last :
        # base case #1
        return False
    else :
        # Find the midpoint of the sequence.
        mid = (last + first) // 2

        # Does the element at the midpoint contain the target?
        if theSeq[mid] == target :
            return True
        # base case #2
        # or does the target precede the element at the midpoint?
        elif target < theSeq[mid] :
            return recBinarySearch( target, theSeq, first, mid - 1 )
        # or does it follow the element at the midpoint?
        else :
            return recBinarySearch( target, theSeq, mid + 1, last )
