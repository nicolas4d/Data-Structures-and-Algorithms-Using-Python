# Finding the location of a target value using the binary search.

# Modified version of the binary search that returns the index within
# a sorted sequence indicating where the target should be located.
def findSortedPosition( theList, target ):
    low = 0
    high = len(theList) - 1
    while low <= high :
        mid = (high + low) // 2
        if theList[mid] == target :
            return mid # Index of the target.
        elif target < theList[mid] :
            high = mid - 1
        else :
            low = mid + 1
    # Index where the target value should be
    return low

sortedList = [2, 4, 5, 10, 13, 18, 23, 29, 31, 51, 64]
targetIndex = findSortedPosition(sortedList, 25)
print(targetIndex) # 7

