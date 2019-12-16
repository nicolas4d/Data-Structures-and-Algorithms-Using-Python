# Implementation of the merge sort algorithm for use with Python list.

from mergeSortedLists import mergeSortedLists

def pythonMergeSort(theList):
    # Check the base cace - the list contains a single item.
    if len(theList) <= 1:
        return theList
    else :
        # Compute the midpoint
        mid = len(theList) // 2

        # Split the list and perfom the recursive step.
        leftHalf = pythonMergeSort(theList[:mid])
        rightHalf = pythonMergeSort(theList[mid:])

        # Merge the two ordered sub-lists.
        newList = mergeSortedLists(leftHalf, rightHalf)
        return newList

print()

theList = [9, 8, 7, 8, 1, 2, 4, 5]
print(pythonMergeSort(theList))



