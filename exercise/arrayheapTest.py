import unittest
from arrayheap import *

class TestMaxHeap(unittest.TestCase):
    def test_init(self):
        mh = MaxHeap(4)

    def test_len(self):
        mh = MaxHeap(4)
        self.assertEqual(len(mh), 0)

    def test_capacity(self):
        mh = MaxHeap(4)
        self.assertEqual(mh.capacity(), 4)

    def test_add(self):
        mh = MaxHeap(4)
        mh.add(4)
        mh.add(3)
        mh.add(2)
        mh.add(1)
        self.assertEqual(mh._elements[0], 4)

    def test_extract(self):
        mh = MaxHeap(4)
        mh.add(4)
        mh.add(3)
        mh.add(2)
        mh.add(1)
        self.assertEqual(mh.extract(), 4)

if __name__ == '__main__':
    unittest.main()
