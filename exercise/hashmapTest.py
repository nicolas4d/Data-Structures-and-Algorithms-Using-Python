import unittest
from hashmap import *
from hashmap import _MapEntry

class TestHashmap(unittest.TestCase):
    def test_init(self):
        hm = Hashmap()

    def test_len(self):
        hm = Hashmap()
        self.assertEqual(len(hm), 0)

    def test_contains(self):
        hm = Hashmap()
        self.assertEqual(1 in hm, False)

    def test_add(self):
        hm = Hashmap()

        hm.add(1, 2)
        self.assertEqual(1 in hm, True)

    def test_valueOf(self):
        hm = Hashmap()
        hm.add(1, 1)
        self.assertEqual(hm.valueOf(1), 1)

    def test__findSlot(self):
        hm = Hashmap()

        # for insert
        self.assertEqual(hm._findSlot(1, True), 1)

    def test_rehash(self):
        hm = Hashmap()
        self.assertEqual(len(hm._table), 7)

        hm._rehash()
        self.assertEqual(len(hm._table), 15)

    def test_hash1(self):
        hm = Hashmap()
        self.assertEqual(hm._hash1(1), 1)

    def test_hash2(self):
        hm = Hashmap()
        self.assertEqual(hm._hash2(1), 2)

    def test_remove(self):
        hm = Hashmap()
        hm.add(1, 1)
        self.assertEqual(1 in hm, True)

        hm.remove(1)
        self.assertEqual(1 not in hm, True)

    def test_iter(self):
        print("test_iter:")

        hm = Hashmap()
        hm.add(1, 1)
        hm.add(2, 2)

        for curKey in hm:
            print(curKey)

if __name__ == '__main__':
    unittest.main()
