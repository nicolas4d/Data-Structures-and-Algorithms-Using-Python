class Queue:
    # Creates an empty queue.
    def __init__(self):
        self._qList = list()

    def __len__(self):
        return len(self._qList)

    # Returns True if the queue is empty.
    def isEmpty(self):
        return len(self) == 0

    # Adds the given item to the queue.
    def enqueue(self, item):
        self._qList.append(item)

    # Removes and return the first item in the queue.
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from empty queue."
        return self._qList.pop(0)

    # Reverse the items in the queue.
    def reverse(self):
        reverList = list()

        ndx = len(self) - 1

        # copy list to new list in reverse order
        while ndx >= 0:
            item = self._qList[ndx]
            reverList.append(item)
            ndx -= 1

        self._qList = reverList
