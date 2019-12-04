# Implementation of the Queue ADT using a Python list.
class Queue :
    # Creates an empty queue.
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
    # O(n) :: worst case list need to expend
    # When used in sequence, the enqueue operation has an amortized cost of
    # O(1).
    def enqueue( self, item ):
        self._qList.append( item )

    # Removes and returns the first item in the queue.
    # O(n)
    def dequeue( self ):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        return self._qList.pop( 0 )
