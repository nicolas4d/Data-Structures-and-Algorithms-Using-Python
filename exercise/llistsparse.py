# Implementation of the Sparse matrix ADT using an array of linked lists.
from array import Array

class SparseMatrix:
    def __init__(self, numRows, numCols):
        self._numCols = numCols
        self._listOfRows = Array(numRows)

    def numRows(self):
        return len(self._listOfRows)

    def numCols(self):
        return self._numCols

    # O(k)
    def __getitem__(self, ndxTuple):
        curNode = self._listOfRows[ndxTuple[0]]

        while curNode is not None:
            if curNode.col == ndxTuple[1] :
                return curNode.value

            curNode = curNode.next

        return None

    # O(k)
    def __setitem__(self, ndxTuple, value):
        row = ndxTuple[0]
        col = ndxTuple[1]
        predNode = None
        curNode = self._listOfRows[row]

        while curNode is not None and curNode.col != col:
            predNode = curNode
            curNode = curNode.next

        if curNode is not None and curNode.col == col:
            if value == 0.0:
                if curNode == self._listOfRows[row]:
                    self._listOfRows[row] = curNode.next
                else :
                    predNode.next = curNode.next
            else:
                curNode.value = value
        elif value != 0.0:
            newNode = _MatrixElementNode(col, value)
            newNode.next = curNode
            if curNode == self._listOfRows[row]:
                self._listOfRows[row] = newNode
            else:
                predNode.next = newNode

    def scaleBy(self, scalar):
        for row in range(self.numRows):
            curNode = self._listOfRows[row]
            while curNode is not None:
                curNode.value *= scalar
                curNode = curNode.next

    # transpose matrix
    # O(kn ^ 2) k is the number of non-zero value
    def transpose(self):
        newSparceMatrix = SparseMatrix(self.numCols(), self.numRows())

        for i in range(self.numRows()):
            for j in range(self.numCols()):
                if self[i, j] != None:
                    newSparceMatrix[j, i] = self[i, j]

        return newSparceMatrix

    # O(k) . o(kn) if use set/get
    def __add__(self, rhsMartrix):
        assert rhsMartrix.numRows() == self.numRows() and \
            rhsMartrix.numCols() == self.numCols, \
            "Matrix sizes not compatable for adding."

        newMatrix = SparseMatrix(self.numRows(), self.numCols())

        for row in range(self.numRows()):
            curNode = self._listOfRows[row]
            while curNode is not None:
                newMatrix[row, curNode.col] = curNode.value
                curNode = curNode.next

        for row in range(rhsMartrix.numRows()):
            curNode = rhsMartrix._listOfRows[row]
            while curNode is not None:
                value = newMatrix[row, curNode.col]
                value += curNode.value
                newMatrix[row, curNode.col] = value
                curNode = curNode.next

        return newMatrix

    # subtract matrix
    # O(kn) 
    def __sub__(self, rhsMatrix):
        # print(rhsMatrix.numRows(), rhsMatrix.numCols())
        # print(self.numRows(), self.numCols())
        # print(rhsMatrix.numRows() == self.numRows())
        # print(rhsMatrix.numCols() == self.numCols())

        assert rhsMatrix.numRows() == self.numRows() and \
            rhsMatrix.numCols() == self.numCols(), \
            "Matrix sizes not compatable for subing."

        # print("after assert of sub")

        newMatrix = SparseMatrix(self.numRows(), self.numCols())

        for row in range(self.numRows()):
            curNode = self._listOfRows[row]
            while curNode is not None:
                newMatrix[row, curNode.col] = curNode.value
                curNode = curNode.next

        for row in range(rhsMatrix.numRows()):
            curNode = rhsMatrix._listOfRows[row]
            while curNode is not None:
                value = newMatrix[row, curNode.col]
                value -= curNode.value
                newMatrix[row, curNode.col] =value
                curNode = curNode.next

        return newMatrix

    # O(n ^ 3)
    def __mul__(self, rhsMatrix):
        assert self.numCols() == rhsMatrix.numRows(), \
            "multiple has to equal left c and right r"

        newMatrix = SparseMatrix(self.numRows(), rhsMatrix.numCols())

        for i in range(newMatrix.numRows()):
            for j in range(newMatrix.numCols()):
                newMatrix[i, j] = self._mul_value(rhsMatrix, i)

        return newMatrix

    def _mul_value(self, rhsMatrix, row):
        value = 0

        for ndxCol in range(self.numCols()):
            if self[row, ndxCol] is not None and \
               rhsMatrix[ndxCol, row] is not None:
                value += self[row, ndxCol] * rhsMatrix[ndxCol, row]

        return value

    def __iter__(self):
        return _SparseMatrixIter(self._listOfRows)

class _MatrixElementNode:
    def __init__(self, col, value):
        self.col = col
        self.value = value
        self.next = next

class _SparseMatrixIter:
    def __init__(self, listOfRows):
        self._listOfRows = listOfRows
        self._ndxOfRow = 0
        self.curNode = self._listOfRows[self._ndxOfRow]

    def __iter__(self):
        return self

    def __next__(self):
        # iterates row
        if self.curNode is not None and self.curNode.value is not None:
            value = self.curNode.value
            self.curNode = self.curNode.next

            # set next row
            if self.curNode is None and \
               self._ndxOfRow + 1 < len(self._listOfRows):
                self._ndxOfRow += 1
                self.curNode = self._listOfRows[self._ndxOfRow]

            return value
        else :
            raise StopIteration

