class ListNode:
    def __init__(self, data):
        self.data = data

a = ListNode("a")
b = ListNode("b")
c = ListNode("c")

print(a.data)
print(b.data)
print(c.data)

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

a.next = b
b.next = c

b = None
c = None

print(a.data)
print(a.next.data)
print(a.next.next.data)
