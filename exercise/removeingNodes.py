from linkedStructuresIntroduction import ListNode

def removeNode(head, data):
    predNode = None
    curNode = head

    while curNode is not None and curNode.data != data:
        predNode = curNode
        curNode = curNode.next

    if curNode is not None:
        if curNode is head:
            head = curNode.next
        else:
            predNode.next = curNode.next

a = ListNode("a")
b = ListNode("b")
c = ListNode("c")

a.next = b
b.next = c

print("remove node :")
removeNode(a, "b")
print(a.data)
print(a.next.data)



