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

curNode.next.next = curNode.next.next.next

print()
print(head.item)
print(head.next.item)
print(head.next.next.item)
print(head.next.next.next.item)
# print(head.next.next.next.next.item)

