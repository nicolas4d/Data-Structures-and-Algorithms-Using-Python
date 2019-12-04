def findNeg( intList ):
    n = len(intList)
    for i in range( n ) :
        if intList[i] < 0 :
            return i
    return None
