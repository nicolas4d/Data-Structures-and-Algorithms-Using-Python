import unittest
from llistsparse import *
from llistsparse import _MatrixElementNode

class TestSparseMatrix(unittest.TestCase):
    def test_init(self):
        sparseMatrix = SparseMatrix(4, 4)
        self.assertEqual(sparseMatrix._numCols, 4)
        self.assertEqual(len(sparseMatrix._listOfRows), 4)

    def test_numRow(self):
        sm = SparseMatrix(4, 4)
        self.assertEqual(sm.numRows(), 4)

    def test_numCols(self):
        sm = SparseMatrix(4, 4)
        self.assertEqual(sm.numCols(), 4)

    def test_getitem(self):
        sm = SparseMatrix(4, 4)
        sm[0, 0] = 0.01
        self.assertEqual(sm[0, 0], 0.01)

        self.assertEqual(sm[0, 1], None)

    def test_setitem(self):
        sm = SparseMatrix(4, 4)
        sm[0, 0] = 0.01
        self.assertEqual(sm._listOfRows[0].value, 0.01)

    def test_transpose(self):
        sm = SparseMatrix(1, 2)
        newSm = sm.transpose()
        # print(newSm)
        # print(newSm.numRows())
        # print(newSm.numCols())

        sm[0, 0] = 0.01
        sm[0, 1] = 0.1

        newSm = sm.transpose()

        # print(newSm[0, 0])
        # print(newSm[1, 0])

    def test_sub(self):
        sm = SparseMatrix(2, 2)
        sm[0, 0] = 0.01
        sm[0, 1] = 0.1
        sm[1, 0] = 1
        sm[1, 1] = 1.1

        othersm = SparseMatrix(2, 2)
        othersm[0, 0] = 1

        newsm = sm - othersm

        self.assertEqual(newsm[0, 0], -0.99)

    def test_mul(self):
        sm = SparseMatrix(2, 3)
        other = SparseMatrix(3, 2)

        sm[0, 0] = 1
        sm[0, 1] = 1
        sm[0, 2] = 1
        sm[1, 0] = 1
        sm[1, 1] = 1
        sm[1, 2] = 1
        other[0, 0] = 1
        other[0, 1] = 1
        other[1, 0] = 1
        other[1, 1] = 1
        other[2, 0] = 1
        other[2, 1] = 1

        new = sm * other
        self.assertEqual(new[0, 0], 3)

        print()
        print("test_mul:")

        for value in new:
            print(value, end=" ")

        print()

    def test_iter(self):
        print("iter:")

        sm = SparseMatrix(4, 4)

        sm[0, 0] = 0
        sm[0, 1] = 11
        sm[0, 2] = 2
        sm[0, 3] = 3
        sm[1, 0] = 0
        sm[1, 1] = 1
        sm[1, 2] = 2
        sm[1, 3] = 3
        sm[2, 0] = 0
        sm[2, 1] = 1
        sm[2, 2] = 2
        sm[2, 3] = 3
        sm[3, 0] = 0
        sm[3, 1] = 1
        sm[3, 2] = 2
        sm[3, 3] = 3

        for item in sm:
            print(item, end=" ")

class Test_MatrixElementNode(unittest.TestCase):
    def test_ini(self):
        men = _MatrixElementNode(4, 4)

if __name__ == '__main__':
    unittest.main()
