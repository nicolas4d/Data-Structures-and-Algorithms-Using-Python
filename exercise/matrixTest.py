from matrix import Matrix
import unittest

class MatrixTest(unittest.TestCase):
    def test__init__(self):
        matrix = Matrix(2, 2)
        # print(matrix._theGrid[0, 0])
        self.assertEqual(matrix._theGrid[0, 0], 0)
        self.assertEqual(matrix._theGrid[0, 1], 0)
        self.assertEqual(matrix._theGrid[1, 0], 0)
        self.assertEqual(matrix._theGrid[1, 1], 0)

    def test_numRows(self):
        matrix = Matrix(2, 2)
        self.assertEqual(matrix.numRows(), 2)

    def test_numCols(self):
        matrix = Matrix(2, 2)
        self.assertEqual(matrix.numCols(), 2)

    def test__getitem__(self):
        matrix = Matrix(2, 2)
        self.assertEqual(matrix[0, 0], 0)

    def test__setitem__(self):
        matrix = Matrix(2, 2)
        matrix[0, 0] = 1
        self.assertEqual(matrix[0,0], 1 )

    def test_scaleBy(self):
        matrix = Matrix(2, 2)
        matrix[0, 0] = 1
        matrix.scaleBy(10)
        self.assertEqual(matrix[0, 0], 10)

    def test__add__(self):
        matrix = Matrix(2, 2)
        rhsMatrix = Matrix(2, 2)
        matrix[0, 0] = 1
        rhsMatrix[0, 0] = 1
        newMatrix = matrix + rhsMatrix
        self.assertEqual(newMatrix[0, 0], 2)

    def test__sub__(self):
        matrix = Matrix(2, 2)
        rhsMatrix = Matrix(2, 2)
        matrix[0, 0] = 10
        rhsMatrix[0, 0] = 5
        newMatrix = matrix - rhsMatrix
        self.assertEqual(newMatrix[0, 0], 5)

    def test_multElement(self):
        matrix = Matrix(3, 2)
        rhsMatrix = Matrix(2, 3)
        matrix[0, 0] = 0
        matrix[0, 1] = 1
        rhsMatrix[0, 0] = 6
        rhsMatrix[1, 0] = 9
        element = matrix._multElement(rhsMatrix, 0, 0)
        self.assertEqual(element, 9)

    def test__mult__(self):
        matrix = Matrix(3, 2)
        rhsMatrix = Matrix(2, 3)
        matrix[0, 0] = 0
        matrix[0, 1] = 1
        rhsMatrix[0, 0] = 6
        rhsMatrix[1, 0] = 9
        newMatrix = matrix.__mult__(rhsMatrix)
        self.assertEqual(newMatrix[0, 0], 9)
        self.assertEqual(newMatrix[0, 1], 0)

    def test_transpose(self):
        matrix = Matrix(3, 2)
        matrix[0, 1] = 1
        # print(matrix)
        transposeMatrix = matrix.transpose()
        # print(matrix)
        self.assertEqual(transposeMatrix.numRows(), 2)
        self.assertEqual(transposeMatrix.numCols(), 3)
        self.assertEqual(transposeMatrix[1, 0], 1)

unittest.main()
