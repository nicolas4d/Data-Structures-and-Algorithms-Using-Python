from linkedStructuresIntroduction import ListNode

def prependNewNode(head, data):
    newNode = ListNode(data)
    newNode.next = head
    head = newNode
    return head

a = ListNode("a")
b = ListNode("b")
a.next = b

print("prependNewNode:")
head = prependNewNode(a, "prependNewNode")
print(head.data)
print(head.next.data)
print(head.next.next.data)
