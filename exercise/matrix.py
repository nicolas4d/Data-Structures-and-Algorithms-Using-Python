from array import Array2D

class Matrix:
    def __init__(self, numRows, numCols):
        "Creates a matrix"
        self._theGrid = Array2D(numRows, numCols)
        self._theGrid.clear(0)

    def numRows(self):
        return self._theGrid.numRows()

    def numCols(self):
        return self._theGrid.numCols()

    def __getitem__(self, ndxTuple):
        return self._theGrid[ndxTuple[0], ndxTuple[1]]

    def __setitem__(self, ndxTuple, scalar):
        self._theGrid[ndxTuple[0], ndxTuple[1]] = scalar

    def scaleBy(self, scalar):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                self._theGrid[r, c] *= scalar

    def __add__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and \
            rhsMatrix.numCols() == self.numCols(), \
            "Matrix sizes not capable for the add operation"

        newMatrix = Matrix(self.numRows(), self.numCols())

        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r, c] = self[r, c] + rhsMatrix[r, c]

        return newMatrix

    def __sub__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and \
            rhsMatrix.numCols() == self.numCols(), \
            "Matrix sizes noot capable for the add operation."

        newMatrix = Matrix(self.numRows(), self.numCols())

        for r in range(self.numRows()):
            for c  in range(self.numCols()):
                newMatrix[r, c] = self[r, c] - rhsMatrix[r, c]

        return newMatrix

    def __mult__(self, rhsMatrix):
        "multiple."
        assert self.numCols() == rhsMatrix.numRows(), \
            "must be left columns == right rows."

        newMatrix = Matrix(self.numRows(), rhsMatrix.numCols())

        for r in range(newMatrix.numRows()):
            for c in range(newMatrix.numCols()):
                newMatrix[r, c] = self._multElement(rhsMatrix, r, c)

        return newMatrix

    def _multElement(self, rhsMatrix, row, col):
        "get element of multiple operation."
        element = 0

        for c in range(self.numCols()):
            element += self[row, c] * rhsMatrix[c, col]

        return element

    def transpose(self):
        """transpose rows and columns."""
        transposeMatrix = Matrix(self.numCols(), self.numRows())

        for r in range(self.numRows()):
            for c in range(self.numCols()):
                transposeMatrix[c, r] = self[r, c]

        return transposeMatrix
