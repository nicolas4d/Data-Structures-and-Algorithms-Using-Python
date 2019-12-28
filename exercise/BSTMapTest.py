import unittest
from BSTMap import *
from BSTMap import _BSTMapNode

class TestBSTMap(unittest.TestCase):
    def mapNodes(self):
        node1 = _BSTMapNode(1, 1)
        node2 = _BSTMapNode(2, 2)
        node3 = _BSTMapNode(3, 3)
        node4 = _BSTMapNode(4, 4)
        node5 = _BSTMapNode(5, 5)
        node6 = _BSTMapNode(6, 6)
        node7 = _BSTMapNode(7, 7)

        node4.left = node3
        node4.right = node5

        # print(node4.left.key)
        # print(node4.right.key)

        return node4

    def test_init(self):
        m = BSTMap()

    def test_len(self):
        m = BSTMap()
        self.assertEqual(len(m), 0)
        m.add(1, 1)
        m.add(2, 2)
        self.assertEqual(len(m), 2)

    def test_iter(self):
        m = BSTMap()
        m.add(4, 4)
        m.add(1, 1)
        m.add(5, 5)

        for key in m :
            print(key)

    def test_contains(self):
        m = BSTMap()
        self.assertEqual(1 in m, False)
        m.add(1, 1)
        self.assertEqual(1 in m, True)

    def test_valueOf(self):
        m = BSTMap()
        m.add(1, 1)
        self.assertEqual(m.valueOf(1), 1)

    def test_bstSearch(self):
        root = self.mapNodes()

        self.assertEqual(None, None)

        m = BSTMap()
        self.assertEqual(m._bstSearch(root, 4).key, 4)
        self.assertEqual(m._bstSearch(root, 5).key, 5)
        self.assertEqual(m._bstSearch(root, 3).key, 3)

    def test_add(self):
        m = BSTMap()
        m.add(1, 1)
        m.add(2, 2)
        m.add(-1, -1)
        self.assertEqual(m.valueOf(1), 1)

    def test_remove(self):
        m = BSTMap()
        m.add(4, 4)
        m.add(1, 1)
        m.add(5, 5)
        m.remove(4)
        # self.assertEqual(m.valueOf(4), 4)
        m.remove(5)
        # self.assertEqual(m.valueOf(5), 5)
        m.remove(1)
        # self.assertEqual(m.valueOf(1), 1)

        m.add(4, 4)
        m.add(1, 1)
        m.add(5, 5)
        m.remove(1)
        # self.assertEqual(m.valueOf(1), 1)

if __name__ == '__main__':
    unittest.main()
