import unittest
from binaryset import Set

class TestSet(unittest.TestCase):
    def test_init(self):
        set = Set()

    def test_len(self):
        set = Set()
        self.assertEqual(len(set), 0)

    def test_findPosition(self):
        set = Set()
        self.assertEqual(set._findPosition(1), 0)

    def test_contains(self):
        set = Set()
        set.add(1)
        set.add(11)
        self.assertEqual(0 in set, False)
        self.assertEqual(11 in set, True)

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

    def test_iter(self):
        set = Set()
        set.add(1)
        for el in set:
            pass

    def test_isSubsetOf(self):
        set = Set()
        set.add(1)
        otherSet = Set()
        otherSet.add(1)
        self.assertEqual(set.isSubsetOf(otherSet), True)

    def test_eq(self):
        set = Set()
        set.add(1)
        otherSet = Set()
        otherSet.add(1)
        self.assertEqual(set == otherSet, True)

    def test_union(self):
        set = Set()
        set.add(1)
        set.add(2)
        otherset = Set()
        otherset.add(2)
        otherset.add(3)
        otherset.add(4)
        otherset.add(5)
        newset = set.union(otherset)

        self.assertEqual(1 in newset, True)
        self.assertEqual(2 in newset, True)
        self.assertEqual(3 in newset, True)

    def test_isSubsetOf(self):
        set = Set()
        set.add(1)
        otherset = Set()
        otherset.add(1)
        self.assertEqual(set.isSubsetOf(otherset), True)
        otherset.add(2)
        self.assertEqual(set.isSubsetOf(otherset), True)
        set.add(3)
        self.assertEqual(set.isSubsetOf(otherset), False)

    def test_intersect(self):
        set = Set()
        set.add(1)
        otherset = Set()
        otherset.add(1)
        intersetion = set.intersect(otherset)
        self.assertEqual(1 in intersetion, True)
        otherset.add(2)
        intersetion = set.intersect(otherset)
        self.assertEqual(1 in intersetion, True)
        set.add(3)
        self.assertEqual(1 in intersetion, True)

    def test_difference(self):
        set = Set()
        set.add(1)
        otherset = Set()
        otherset.add(1)
        diffset = set.difference(otherset)
        self.assertEqual(1 not in diffset, True)

        set.add(11)
        otherset.add(22)
        diffset = set.difference(otherset)
        self.assertEqual(11 in diffset, True)
        self.assertEqual(22 not in diffset, True)

if __name__ == '__main__':
    unittest.main()
