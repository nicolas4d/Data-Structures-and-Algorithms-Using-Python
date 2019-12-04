# Implementation of the linear search on a sorted sequence.
def sortedLinearSearch( theValues, item ) :
    n = len( theValues )
    for i in range( n ) :
        # If the target is found in the ith element, return True
        if theValues[i] == item :
            return True
        # If target is larger than the ith element, it's not in the sequence.
        elif theValues[i] > item :
            return False
    # The item is not in the sequence.
    return False

