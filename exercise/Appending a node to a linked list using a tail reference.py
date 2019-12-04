from usingTailReference import ListNode

# Given the head and tail pointers, adds an item to the end  a linked list.
def appendTail(head, tail, item):
    newNode = ListNode(item)

    if head is None:
        head = newNode
    else:
        tail.next = newNode

    tail = newNode

a = ListNode("a")
b = ListNode("b")

a.next = b

appendTail(a, b, "c")

print(a.item)
print(a.next.item)
print(a.next.next.item)
