def binarySearch(theValues, target):
    low = 0
    high = len(theValues) - 1

    while low <= high:
        mid = (low + high) // 2

        if theValues[mid] == target:
            return True
        elif theValues[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return False

theValues = [1, 2, 3, 5, 6, 44, 66, 22, 55]
print(binarySearch(theValues, 66))
print(binarySearch(theValues, 77))
