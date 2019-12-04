# Implementation of the unbounded Priority Queue ADT using a Python list
# with new items appended to the end.
class PriorityQueue :
    # Create an empty unbounded priority queue.
    def __init__( self ):
        self._qList = list()

    # Returns True if the queue is empty.
    # O(1)
    def isEmpty( self ):
        return len( self ) == 0

    # Returns the number of items in the queue.
    # O(1)
    def __len__( self ):
        return len( self._qList )

    # Adds the given item to the queue.
    # worst O(n) , O(1) amortized cost
    def enqueue( self, item, priority ):
        # Create a new instance of the storage class and append it to the list.
        entry = _PriorityQEntry( item, priority )
        self._qList.append( entry )

    # Removes and returns the first item in the queue.
    # O(n)
    def dequeue( self ) :
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        # Find the entry with the highest priority.
        highest = self._qList[i].priority
        for i in range( self.len() ) :
            # See if the ith entry contains a higher priority (smaller integer).
            if self._qList[i].priority < highest :
                highest = self._qList[i].priority

        # Remove the entry with the highest priority and return the item.
        entry = self._qList.pop( highest )
        return entry.item

# Private storage class for associating queue items with their priority.
class _PriorityQEntry( object ):
    def __init__( self, item, prioity ):
        self.item = item
        self.priority = priority
