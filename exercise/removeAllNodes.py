from usingTailReference import ListNode

def removeAll(head):
    curNode = head

    while curNode is not None:
        succNode = curNode.next
        curNode.next = None
        curNode.item = None
        curNode = None
        curNode = succNode

a = ListNode("a")
b = ListNode("b")
a.next = b

removeAll(a)

print(a)
print("is a == None", a is None)

print(a.item)
