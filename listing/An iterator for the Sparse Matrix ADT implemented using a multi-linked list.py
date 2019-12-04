# Defines a Python iterator for the Sparse Matrix ADT implemented using
# an array of linked lists.
class _SparseMatrixIterator :
    def __init__( self, rowArray ):
        self._rowArray = rowArray
        self._curRow = 0
        self._curNode = None
        self._findNextElement()

    def __iter__( self ):
            return self

    def next( self ):
        if self._curNode is None :
            raise StopIteration
        else :
            value = self._curNode.value
            self._curNode = self._curNode.next
            if self._curNode is None :
                self._findNextElement()
            return value

    def _findNextElement( self ):
        i = self._curRow

        while i < len( self._rowArray ) and \
              self._rowArray[i] is None :
            i += 1

        self._curRow = i

        if i < len( self._rowArray ) :
            self._currNode = self._rowVector[i]
        else :
            self._currNode = None
