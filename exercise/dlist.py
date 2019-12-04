# ordered doble linked list.
class DList:
    # O(1)
    def __init__(self):
        "Cteates an empty doble linked list. "
        self._head = None
        self._tail = None
        self._probe = None
        self._count = 0

    # O(1)
    def revTraversal(self):
        curNode = self._tail

        while curNode is not None:
            print(curNode.data)
            curNode = curNode.prev

    # search for the given target
    # O(n)
    def search(self, target):
        # Make sure the list is not empty
        if self._head is None:
            return False
         
        # If probe is null, initialize it to the first node.
        elif self._probe is None:
            self._probe = self._head

        if target < self._probe.data:
            while self._probe is not None and target <= self._probe.data:
                if target == self._probe.data:
                    return True
                else :
                    self._probe = self._probe.prev
        else :
            while self._probe is not None and target >= self._probe.data:
                if target == self._probe.data:
                    return True
                else :
                    self._probe = self._probe.next

        # If the target is not found in the list, return False
        return False

    # Given a head and tail reference and a new value, add the new value to a
    # sorted doubly linked list
    # O(n)
    def add(self, value):
        newNode = DListNode(value)

        # Empty list
        if self._head is None:
            self._head = newNode
            self._tail = self._head
        # insert before head
        elif value < self._head.data:
            newNode.next = self._head
            self._head.prev = newNode
            self._head = newNode
        # insert after tail
        elif value > self._head.data:
            newNode.prev = self._tail
            self._tail.next = newNode
            self._tail = newNode
        # insert in the middle
        else :
            node = head
            while node is not None and node.data < value:
                node = node.next

            newNode.next = node
            newNode.prev = node.prev
            node.prev.next = newNode
            node.prev = newNode

# Doble linked list node
class DListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
