def findSortedPosition(theList, target):
    low = 0
    high = len(theList) - 1
    while low <= high:
        mid = (low + high) // 2
        if theList[mid] == target:
            return mid
        elif target < theList[mid]:
            high = mid - 1
        else :
            low = mid + 1

    return low

sortedList = [2, 4, 5, 10, 13, 18, 23, 29, 31, 51, 64]
targetIndex = findSortedPosition(sortedList, 25)
print(targetIndex) # 7

def findSortedPositionFindFirstOccur(theValues, target):
    low = 0
    high = len(theValues) - 1

    while low <= high:
        mid = (low + high) // 2

        if theValues[mid] == target:
            print("==")
            if mid - 1 > 0 and theValues[mid - 1] == target:
                high = mid - 1
            else :
                return mid
        elif theValues[mid] > target:
            high = mid - 1
        else :
            low = mid + 1

    print("return ")
    return low

print("findSortedPositionFindFirstOccur")
theValues = [1, 2, 3, 5, 6, 66, 66, 66,77,88,99]
print(findSortedPositionFindFirstOccur(theValues, 66)) # 55

