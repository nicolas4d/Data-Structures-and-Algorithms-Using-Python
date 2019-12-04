# Implementation of the unbounded Priority Queue ADT  using a Python list.
# with new items append to the end
class PriorityQueue:
    # Create and empty unbounded priority queue.
    def __init__(self):
        self._qlist = list()

    # Returns True if the queue is empty
    # O(1)
    def isEmpty(self):
        return len(self) == 0

    # Returns the number of items in the queue.
    # O(1)
    def __len__(self):
        return len(self._qlist)

    # Adds the given item to the queue.
    # worst O(n), O(1) amortized cost
    def enqueue(self, item, priority):
        entry = _PriorityQEntry(item, priority)
        self._qlist.append(entry)

    # Removes and returns the first item in the queue
    # O(n)
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."

        highest = self._qlist[0].priority
        ndx = 0

        # Find the entry with the highest priority.
        for i in range(len(self)):
            if self._qlist[i].priority < highest:
                highest = self._qlist[i].priority
                ndx = i

        # Remove the entry with the highest priority and return the item
        entry = self._qlist.pop(ndx)
        return entry.item

# Private storage class for associating queue items with their priority.
class _PriorityQEntry(object):
    def __init__(self, item, prioity):
        self.item = item
        self.priority = prioity
