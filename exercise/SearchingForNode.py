from linkedStructuresIntroduction import ListNode

def unorderedSearch(head, target):
    curNode = head

    while curNode is not None and curNode.data != target:
        curNode = curNode.next

    return curNode is not None

a = ListNode("a")
b = ListNode("b")

a.next = b

print("searching for Node:")
print(unorderedSearch(a, "a"))
