import unittest
from dllist import *

class TestDList(unittest.TestCase):
    def test_init(self):
        dll = DList()

    def test_revTraversal(self):
        dll = DList()
        dll.revTraversal()

    def test_search(self):
        dll = DList()
        dll.search(1)

    def test_add(self):
        dl = DList()
        dl.add(1)
        self.assertEqual(dl.search(1), True)

if __name__ == '__main__':
    unittest.main()
