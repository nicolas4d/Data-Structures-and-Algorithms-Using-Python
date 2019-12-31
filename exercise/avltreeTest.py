import unittest
from avltree import *
from avltree import _AVLMapNode

class TestAVLMap(unittest.TestCase):
    def test_init(self):
        avlmap = AVLMap()

    def test_len(self):
        avlmap = AVLMap()
        self.assertEqual(len(avlmap), 0)

    def test_contains(self):
        avlmap = AVLMap()
        self.assertEqual(1 in avlmap, False)

    def test_valueOf(self):
        avlmap = AVLMap()

        # no key test
        # self.assertEqual(avlmap.valueOf(1), 1)

    def test_avlRotateRight(self):
        # Create avlmapnodes
        node3 = _AVLMapNode(3, 3)
        node2 = _AVLMapNode(2, 2)
        node1 = _AVLMapNode(1, 1)

        node3.left = node2
        node2.left = node1

        avlmap = AVLMap()
        rootNode = avlmap._avlRotateRight(node3)

        self.assertEqual(rootNode.key, 2)

        curNode = rootNode.left
        self.assertEqual(curNode.key, 1)
        self.assertEqual(curNode.value, 1)

        curNode = rootNode.right
        self.assertEqual(curNode.key, 3)
        self.assertEqual(curNode.value, 3)

    def test_avlRotateLeft(self):
        # Create avlmapnodes
        node3 = _AVLMapNode(3, 3)
        node2 = _AVLMapNode(2, 2)
        node1 = _AVLMapNode(1, 1)

        node3.right = node2
        node2.right = node1

        avlmap = AVLMap()
        rootNode = avlmap._avlRotateLeft(node3)

        self.assertEqual(rootNode.key, 2)

        curNode = rootNode.right
        self.assertEqual(curNode.key, 1)
        self.assertEqual(curNode.value, 1)

        curNode = rootNode.left
        self.assertEqual(curNode.key, 3)
        self.assertEqual(curNode.value, 3)

    def Create_case_3_nodes(self):
        # Create avlmapnodes
        nodeP = _AVLMapNode("P", "P")
        nodePR = _AVLMapNode("PR", "PR")
        nodeC = _AVLMapNode("C", "C")
        nodeCL = _AVLMapNode("CL", "CL")
        nodeG = _AVLMapNode("G", "G")
        nodeGL = _AVLMapNode("GL", "GL")
        nodeGR = _AVLMapNode("GR", "GR")

        nodeP.right = nodePR
        nodeP.left = nodeC
        nodeC.left = nodeCL
        nodeC.right = nodeG
        nodeG.left = nodeGL
        nodeG.right = nodeGR

        nodeP.bfactor = LEFT_HIGH
        nodeC.bfactor = RIGHT_HIGH
        nodeG.bfactor = EQUAL_HIGH

        return nodeP

    def Create_case_4_nodes(self):
        # Create avlmapnodes
        nodeP = _AVLMapNode("P", "P")
        nodePL = _AVLMapNode("PL", "PL")
        nodeC = _AVLMapNode("C", "C")
        nodeCR = _AVLMapNode("CR", "CR")
        nodeG = _AVLMapNode("G", "G")
        nodeGL = _AVLMapNode("GL", "GL")
        nodeGR = _AVLMapNode("GR", "GR")

        nodeP.left = nodePL
        nodeP.right = nodeC
        nodeC.right = nodeCR
        nodeC.left = nodeG
        nodeG.left = nodeGL
        nodeG.right = nodeGR

        nodeP.bfactor = LEFT_HIGH
        nodeC.bfactor = LEFT_HIGH

        return nodeP

    def test_avlLeftBalance(self):
        # case 1
        # Create avlmapnodes
        node3 = _AVLMapNode(3, 3)
        node2 = _AVLMapNode(2, 2)
        node1 = _AVLMapNode(1, 1)

        node3.left = node2
        node2.left = node1

        node3.bfactor = EQUAL_HIGH
        node2.bfactor = LEFT_HIGH

        avlmap = AVLMap()
        rootNode = avlmap._avlLeftBalance(node3)

        self.assertEqual(rootNode.key, 2)
        self.assertEqual(rootNode.bfactor, EQUAL_HIGH)

        curNode = rootNode.left
        self.assertEqual(curNode.key, 1)
        self.assertEqual(curNode.bfactor, EQUAL_HIGH)

        curNode = rootNode.right
        self.assertEqual(curNode.key, 3)
        self.assertEqual(curNode.bfactor, EQUAL_HIGH)

        # case 3
        nodeP = self.Create_case_3_nodes()

        # Using avlmapnodes to call function
        avlmap = AVLMap()
        root = avlmap._avlLeftBalance(nodeP)

        # test result
        self.assertEqual(root.key, "G")
        self.assertEqual(root.bfactor, EQUAL_HIGH)

        curNode = root.left
        self.assertEqual(curNode.key, "C")
        self.assertEqual(curNode.bfactor, EQUAL_HIGH)

        curNode = root.left.left
        self.assertEqual(curNode.key, "CL")

        curNode = root.left.right
        self.assertEqual(curNode.key, "GL")

        curNode = root.right
        self.assertEqual(curNode.key, "P")
        self.assertEqual(curNode.bfactor, EQUAL_HIGH)

        curNode = root.right.left
        self.assertEqual(curNode.key, "GR")

        curNode = root.right.right
        self.assertEqual(curNode.key, "PR")

    def test_avlRightBalance(self):
        # case 1
        # Create avlmapnodes
        node3 = _AVLMapNode(3, 3)
        node2 = _AVLMapNode(2, 2)
        node1 = _AVLMapNode(1, 1)

        node3.right = node2
        node2.right = node1

        node3.bfactor = RIGHT_HIGH
        node2.bfactor = RIGHT_HIGH

        avlmap = AVLMap()
        rootNode = avlmap._avlRightBalance(node3)

        self.assertEqual(rootNode.key, 2)
        self.assertEqual(rootNode.bfactor, EQUAL_HIGH)

        curNode = rootNode.right
        self.assertEqual(curNode.key, 1)
        self.assertEqual(curNode.bfactor, EQUAL_HIGH)

        curNode = rootNode.left
        self.assertEqual(curNode.key, 3)
        self.assertEqual(curNode.bfactor, EQUAL_HIGH)

        # # case 4
        nodeP = self.Create_case_4_nodes()

        # Using avlmapnodes to call function
        avlmap = AVLMap()
        root = avlmap._avlRightBalance(nodeP)

        # test result
        self.assertEqual(root.key, "G")
        self.assertEqual(root.bfactor, EQUAL_HIGH)

        curNode = root.right
        self.assertEqual(curNode.key, "C")
        self.assertEqual(curNode.bfactor, EQUAL_HIGH)

        curNode = root.right.right
        self.assertEqual(curNode.key, "CR")

        curNode = root.right.left
        self.assertEqual(curNode.key, "GR")

        curNode = root.left
        self.assertEqual(curNode.key, "P")
        self.assertEqual(curNode.bfactor, EQUAL_HIGH)

        curNode = root.left.right
        self.assertEqual(curNode.key, "GL")

        curNode = root.left.left
        self.assertEqual(curNode.key, "PL")

    def test_avlInsert(self):
        avlmap = AVLMap()

        # test None
        (subtree, taller) = avlmap._avlInsert(None, 1, 1)

        self.assertEqual(subtree.key, 1)
        self.assertEqual(subtree.value, 1)
        self.assertEqual(taller, True)

        # Test already in the tree
        (subtree, taller) = avlmap._avlInsert(subtree, 1, 2)

        self.assertEqual(subtree.key, 1)
        self.assertEqual(subtree.value, 2)
        self.assertEqual(taller, False)

        # navigate to the left
        (subtree, taller) = avlmap._avlInsert(None, 10, 10)
        (subtree, taller) = avlmap._avlInsert(subtree, 9, 9)

        # navigate to the right
        (subtree, taller) = avlmap._avlInsert(None, 10, 10)
        (subtree, taller) = avlmap._avlInsert(subtree, 11, 11)
        (subtree, taller) = avlmap._avlInsert(subtree, 9, 9)
        (subtree, taller) = avlmap._avlInsert(subtree, 8, 8)
        (subtree, taller) = avlmap._avlInsert(subtree, 7, 7)

    def test_add(self):
        avlmap = AVLMap()

        # case 1
        avlmap.add(3, 3)
        avlmap.add(2, 2)
        avlmap.add(1, 1)

        # self.assertEqual(avlmap._root.key, 2)

if __name__ == '__main__':
    unittest.main()
