# Searching for the smallest value in an unsorted sequence.
def findSmallest( theValues ):
    n = len( theValues )
    # Assume the first item is the smallest value.
    smallest = theValues[0]
    # Determine if any other item in the sequence is smaller.
    for i in range( 1, n ) :
        if theList[i] < smallest :
            smallest = theValues[i]
    # Return the smallest found.
    return smallest

