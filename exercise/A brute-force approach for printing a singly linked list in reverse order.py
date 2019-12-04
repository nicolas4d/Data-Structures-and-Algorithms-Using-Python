# Print the contents of a singly linked list in reverse order.
# O(n^2)
def printListBF(head):
    # Count the number of nodes in the list.
    numNodes = 0
    curNode = head

    while curNode is not None:
        curNode = curNode.next
        numNodes += 1

    for i in range(numNodes):
        curNode = head
        for j in range(numNodes - 1 - i):
            curNode = curNode.next

        print(curNode.data)

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

a = ListNode("a")
b = ListNode("b")
c = ListNode("c")
a.next = b
b.next = c

printListBF(a)
