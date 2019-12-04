from usingTailReference import ListNode

# Given the head and tail references, removes a target from a linked list.
def removeTail(head, tail, item):
    predNode = None
    curNode = head

    while curNode is not None and curNode.item != item:
        predNode = curNode
        curNode = curNode.next

    if curNode is not None:
        if curNode is head:
            head = curNode.next
        else:
            predNode.next = curNode.next

        if curNode is tail:
            tail = predNode

a = ListNode("a")
b = ListNode("b")

a.next = b

removeTail(a, b, "b")

print(a.item)
print(a.next.item)
