from usingTailReference import ListNode

head = ListNode(73)
curNode = ListNode(2)
head.next = curNode

tempNode = ListNode(52)
curNode.next = tempNode

tempNode.next = ListNode(18)
tempNode.next.next = ListNode(36)

print(head.item)
print(head.next.item)
print(head.next.next.item)
print(head.next.next.next.item)
print(head.next.next.next.next.item)

newNode = ListNode("22")
newNode.next = curNode.next
curNode.next = newNode

print()
print(head.item)
print(head.next.item)
print(head.next.next.item)
print(head.next.next.next.item)
print(head.next.next.next.next.item)
print(head.next.next.next.next.next.item)
