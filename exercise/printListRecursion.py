# Print the contents of a linked list using recursion.
from listnode import ListNode

# O(n)
def printList(head):
    if head is not None:
        printList(head.next)
        print(head.data)

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c

printList(a)
