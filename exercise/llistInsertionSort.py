# Implementation of the insertion sort algorithm for use with a linked list.

# Sorts a linke list using the technique of the insertion sort. A
# reference to the new ordered list is returned.
def llistInsertionSort(origList):
    # Make sure the list contains at least one node.
    if origList is None:
        return None

    # Iterate through the original list.
    newList = None
    while origList is not None:
        # Assign a temp reference to the first node.
        curNode = origList

        # Advance the original list reference to the next node.
        origList = origList.next

        # Unlink the first node
        curNode.next = None

        # insert into the new ordered list.
        newList = addToSortedList(newList, curNode)

    return newList

# Given the head pointer, insert a value into a sorted linked list.
# Find the insertion point for the new value.
def addToSortedList(head, newNode):
    predNode = None
    curNode = head

    while curNode is not None and newNode.item > curNode.item:
        predNode = curNode
        curNode = curNode.next

    newNode.next = curNode

    # Link the new node into the list
    if curNode is head :
        head = newNode
    else :
        predNode.next = newNode

    return head

class ListNode:
    def __init__(self, item):
        self.item = item
        self.next = None

a = ListNode(4)
b = ListNode(3)
c = ListNode(5)
d = ListNode(1)

a.next = b
b.next = c
c.next = d

print(a.item)
print(a.next.item)
print(a.next.next.item)
print(a.next.next.next.item)
print()

newList = llistInsertionSort(a)

print(newList.item)
print(newList.next.item)
print(newList.next.next.item)
print(newList.next.next.next.item)
