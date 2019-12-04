from usingTailReference import ListNode

def insertSortedList(head, item):
    predNode = None
    curNode = head

    while curNode is not None and curNode.item < item:
        predNode = curNode
        curNode = curNode.next

    newNode = ListNode(item)
    newNode.next = curNode

    if curNode is head:
        head = curNode
    else:
        predNode.next = newNode

a = ListNode("a")
c = ListNode("c")

a.next = c

insertSortedList(a, "b")

print(a.item)
print(a.next.item)
print(a.next.next.item)
