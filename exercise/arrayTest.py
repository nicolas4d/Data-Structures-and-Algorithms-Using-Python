from array import Array2D
from array import MultiArray
import array
import unittest

class Array2DTest(unittest.TestCase):

    def test__init__(self):
        array2d = Array2D(2,2)
        # print(array2d)
        # print(array2d._theRows)
        # print(array2d[0,0])

class MultiArray(unittest.TestCase):
    def test__init(self):
        ma = array.MultiArray(2, 3, 4)
        # print("MultiArray __init__ test : ")
        # print(ma._dims)
        # print(ma._elements)
        # print(len(ma._factors))
        # print(ma._factors[0])

    def test_numDims(self):
        ma = array.MultiArray(2, 2)
        self.assertEqual(ma.numDims(), 2)

    def test_length(self):
        ma = array.MultiArray(2, 3)
        self.assertEqual(ma.length(1), 2)

    def test_clear(self):
        ma = array.MultiArray(2, 3)
        ma.clear("clear")
        self.assertEqual(ma._elements[0], "clear")

    def test_computeIndex(self):
        ma = array.MultiArray(2, 3, 4)
        self.assertEqual(ma._computeIndex((1, 1, 1)), 17)

    def test__computeIndex(self):
        ma = array.MultiArray(2,3,4)
        ma._computeFactors()
        self.assertEqual(ma._factors[0], 12)
        self.assertEqual(ma._factors[1], 4)
        self.assertEqual(ma._factors[2], 1)


unittest.main()
