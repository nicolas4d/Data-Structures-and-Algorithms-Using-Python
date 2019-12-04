# Performs a recursive binary search on a sorted sequence.
def recBinarySearch(target, theSeq, first, last):
    # If the sequence cannot be subdiveded further, we are done.
    if first > last:
        # base case #1
        return False
    else :
        # Find the midpoint of the sequence.
        mid = (first + last) // 2

        # Does the element at the midpoint contain the target?
        if theSeq[mid] == target:
            return True
        # base case #2
        # or does the target precede the element at the midpoint?
        elif target < theSeq[mid]:
            return recBinarySearch(target, theSeq, first, mid - 1)
        else :
            return recBinarySearch(target, theSeq, mid + 1, last)

theSeq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(recBinarySearch(2, theSeq, 0, 9))
print(recBinarySearch(11, theSeq, 0, 9))

