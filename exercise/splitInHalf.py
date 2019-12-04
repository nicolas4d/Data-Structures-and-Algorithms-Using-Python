from usingTailReference import ListNode

def splitInHalf(head):
    curNode = head
    headList = list()

    while curNode is not None:
        headList.append(curNode)
        curNode = curNode.next

    return headList[len(headList) // 2]

a = ListNode("a")
b = ListNode("b")
a.next = b

print(splitInHalf(a).item)

c = ListNode("c")
b.next = c

print(splitInHalf(a).item)
