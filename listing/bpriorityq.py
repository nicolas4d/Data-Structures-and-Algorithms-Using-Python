# Implementation of the bounded Priority Queue ADT using an array of
# queues in which the queues are implemented using a linked list.
from array import Array
from llistqueue import Queue

class BPriorityQueue :
    # Creates an empty bounded priority queue.
    def __init__( self, numLevels ):
        self._qSize = 0
        self._qLevels = Array( numLevels )
        for i in range( numLevels ) :
            self._qLevels[i] = Queue()

    # Returns True if the queue is empty.
    def isEmpty( self ):
        return len( self ) == 0

    # Returns the number of items in the queue.
    def __len__( self ):
        return len( self._qSize )

    # Adds the given item to the queue.
    def enqueue( self, item, priority ):
        assert priority >= 0 and priority < len(self._qLevels), \
            "Invalid priority level."
        self._qLevels[priority].enqueue( item )

    # Removes and returns the next item in the queue.
    # requires O(p) time. we can treats p as constant if p is small.
    def dequeue( self ) :
        # Make sure the queue is not empty.
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        # Find the first non-empty queue.
        i = 0
        p = len(self._qLevels)

        while i < p and not self._qLevels[i].isEmpty() :
            i += 1

        # We know the queue is not empty, so dequeue from the ith queue.
        return self._qLevels[i].dequeue()
