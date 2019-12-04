from usingTailReference import ListNode

def sortedSearch(head, target):
    curNode = head

    while curNode is not None and curNode.item <= target:
        if curNode.item == target:
            return True
        else:
            curNode = curNode.next

    return False

a = ListNode(1)
b = ListNode(2)

a.next = b

print(sortedSearch(a, 2))
