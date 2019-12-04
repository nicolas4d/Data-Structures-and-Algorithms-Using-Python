# Defines a Python iterator for the Sparse Matrix ADT implemented using
# an array of linked lists.
class _SparseMatrixIterator :
    def __init__(self, rowArray):
        self._rowArray = rowArray
        self._curRow = 0
        self._curNode = None
        self._findNextElement()

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNode is not None :
            value = self._curNode.value
            self._curNode = self._curNode.next

            if self._curNode is None:
                self._findNextElement()

            return value
        else :
            raise StopIteration

    def _findNextElement(self):
        i = self._curRow

        while i < len(self._rowArray) and \
            self._rowArray[i] is None:
            i += 1

        self._curRow = i

        if i < len(self._rowArray):
            self._curNode = self._rowArray[i]
        else :
            self._curNode = None

