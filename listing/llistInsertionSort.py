# Implementation of the insertion sort algorithm for use with a linked list.

# Sorts a linked list using the technique of the insertion sort. A
# reference to the new ordered list is returned.
def llistInsertionSort( origList ):
    # Make sure the list contains at least one node.
    if origList is None :
        return None

    # Iterate through the original list.
    newList = None
    while origList is not None :
        # Assign a temp reference to the first node.
        curNode = origList

        # Advance the original list reference to the next node.
        origList = origList.next

        # Unlink the first node and insert into the new ordered list.
        curNode.next = None
        newList = addToSortedList( newList, curNode )

    # Return the list reference of the new ordered list.
    return newList
