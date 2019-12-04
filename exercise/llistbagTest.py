import unittest
from llistbag import *

class llistbagTest(unittest.TestCase):
    def test_init(self):
        bag = Bag()
        self.assertEqual(bag._size, 0)
        self.assertEqual(bag._head, None)

    def test_len(self):
        bag = Bag()
        self.assertEqual(len(bag), 0)

    def test_contains(self):
        bag = Bag()
        self.assertEqual(0 in bag, False)

    def test_add(self):
        bag = Bag()
        bag.add(1)
        self.assertEqual(1 in bag, True)

    def test_remove(self):
        bag = Bag()
        bag.add(1)
        self.assertEqual(1 in bag, True)
        bag.remove(1)
        self.assertEqual(1 not in bag, True)

    def test_iter(self):
        bag = Bag()
        bag.add(1)
        for item in bag:
            self.assertEqual(item, 1)

if __name__ == '__main__':
    unittest.main()
