from array import Array2D
from array import Array2DList
from array import Array
import unittest
import sys

class Array2DTest(unittest.TestCase):
    def test_calculateAllocat(self):
        
        array2d = Array2D(75, 100)
        print(sys.getsizeof(array2d._theRows[0]))

        array2d = Array2D(10000, 25)
        print(sys.getsizeof(array2d))

        array2d = Array2D(10000, 10000)
        print(sys.getsizeof(array2d))

        # array2d list
        array2dlist = Array2DList(75, 100)
        print(sys.getsizeof(array2dlist))

        print(sys.getsizeof(Array(75)))
        print(sys.getsizeof([1] * 75 * 100))

unittest.main()
