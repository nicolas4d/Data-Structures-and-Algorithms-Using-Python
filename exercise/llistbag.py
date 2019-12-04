# Implements the Bag ADT using a singly linked list.
class Bag :
    # Constructs and empty bag
    def __init__(self):
        self._head = None
        self._size = 0

    # Return the number of items in the bag
    def __len__(self):
        return self._size

    # Determines if an item is contained in the bag.
    def __contains__(self, el):
        curNode = self._head

        while curNode is not None and curNode.item != el:
            curNode = curNode.next

        return curNode is not None

    # Adds new item to the bag.
    def add(self, item):
        newNode = _BagListNode(item)
        newNode.next = self._head
        self._head = newNode
        self._size += 1

    # Removes an instance of the item from the bag.
    def remove(self, item):
        predNode = None
        curNode = self._head

        while curNode is not None and curNode.item != item:
            predNode = curNode
            curNode = curNode.next

        # The item has to be in the bag to remove it.
        assert curNode is not None, "The item must be in the bag."

        # Unlink the node and return the item.
        self._size -= 1

        if curNode is self._head:
            self._head = curNode.next
        else :
            predNode = curNode.next

        return curNode.item

    # Returns an iterator for traversing the list of items.
    def __iter__(self):
        return _BagIterator(self._head)

# Defines a private storage class for creating list nodes.
class _BagListNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class _BagIterator:
    def __init__(self, listHead):
        self._curNode = listHead

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNode is not None :
            item = self._curNode.item
            self._curNode = self._curNode.next
            return item
        else :
            raise StopIteration
