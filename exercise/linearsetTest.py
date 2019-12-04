from linearset import Set
import unittest

class SetTest(unittest.TestCase):
    def test__init__(self):
        set = Set()
        # print(set._theElements)
        self.assertEqual(set._theElements, [])

        set = Set(1, 2, 3)
        # print(set._theElements)
        self.assertEqual(set._theElements, [1, 2, 3])

    def test__len__(self):
        set = Set()
        self.assertEqual(len(set), 0)

    def test__contains__(self):
        set = Set()
        self.assertEqual(0 in set, False)

    def test_add(self):
        set = Set()
        set.add(1)
        self.assertEqual(1 in set, True)

    def test_remove(self):
        set = Set()
        set.add(1)
        self.assertEqual(1 in set, True)
        set.remove(1)
        self.assertEqual(1 in set, False)

    def test_isSubsetOf(self):
        set = Set()
        set.add(1)
        otherSet = Set()
        otherSet.add(1)
        self.assertEqual(set.isSubsetOf(otherSet), True)

    def test__eq__(self):
        set = Set()
        set.add(1)
        otherSet = Set()
        otherSet.add(1)
        self.assertEqual(set == otherSet, True)

    def test_nion(self):
        set = Set()
        set.add(1)
        otherSet = Set()
        otherSet.add(2)
        self.assertEqual(2 in set.union(otherSet), True)

    def test_intersect(self):
        set = Set()
        set.add(1)
        set.add(2)
        otherSet = Set()
        otherSet.add(2)
        otherSet.add(3)
        self.assertEqual(2 in set.intersect(otherSet), True)

    def test_difference(self):
        set = Set()
        set.add(1)
        set.add(2)
        otherSet = Set()
        otherSet.add(2)
        self.assertEqual(1 in set.difference(otherSet), True)
        self.assertEqual(2 in set.difference(otherSet), False)

    def test_isEmpty(self):
        set = Set()
        self.assertEqual(set.isEmpty(), True)

    def test_properSubset(self):
        set = Set()
        otherSet = Set()
        set.add(1)
        otherSet.add(1)
        otherSet.add(2)
        self.assertEqual(set.properSubset(otherSet), True)
        set.add(2)
        self.assertEqual(set.properSubset(otherSet), False)

    def test___str__(self):
        set = Set()
        set.add(1)
        set.add(2)
        print(set)

    def test___add__(self):
        set = Set(1)
        otherSet = Set(2)
        newSet = set + otherSet
        self.assertEqual(newSet.__contains__(1), True)
        self.assertEqual(newSet.__contains__(2), True)

    def test_mul(self):
        set = Set(1, 2)
        otherSet = Set(1, 3)
        newSet = set * otherSet
        self.assertEqual(newSet.__contains__(1), True)
        self.assertEqual(newSet.__contains__(2), False)
        self.assertEqual(newSet.__contains__(3), False)

    def test_sub(self):
        set = Set(1, 2)
        otherSet = Set(2)
        newSet = set - otherSet
        self.assertEqual(newSet.__contains__(1), True)
        self.assertEqual(newSet.__contains__(2), False)

    def test_isSubsetOf(self):
        set = Set(1, 2)
        otherSet = Set(1, 2, 3)
        self.assertEqual(set < otherSet, True)


unittest.main()
