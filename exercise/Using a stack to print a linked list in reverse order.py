# Print the contents of a linked list in reverse order using a stack.
from lliststack import Stack
from listnode import ListNode

# O(n)
def printListStack(head):
    # Create a stack to store the items
    s = Stack()

    curNode = head

    # Iterate through the list and push each item onto the stack.
    while curNode is not None:
        s.push(curNode.data)
        curNode = curNode.next

    # Repeatedly pop the items from the stack and print them until the
    # stack is empty.
    while not s.isEmpty():
        item = s.pop()
        print(item)

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c

printListStack(a)
