from linkedStructuresIntroduction import ListNode

a = ListNode("a")
b = ListNode("b")

a.next = b

def traversal(head):
    curNode = head

    while curNode is not None:
        print(curNode.data)
        curNode = curNode.next

print("traversal :")
print(a.data)
print(a.next.data)
