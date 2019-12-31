# Constants for the balance factors.
LEFT_HIGH = 1
EQUAL_HIGH = 0
RIGHT_HIGH = -1

# Implementation of the Map ADT using an AVL tree.
class AVLMap:
    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def __contains__(self, key):
        return self._bstSearch(self._root, key) is not None

    def add(self, key, value):
        node = self._bstSearch(self._root, key)

        if node is not None :
            node.value = value
            return False
        else :
            (self._root, tmp) = self._avlInsert(self._root, key, value)
            self._size += 1
            return True

    def valueOf(self, key):
        node = self._bstSearch(self._root, key)
        assert node is not None, "Invalid map key."
        return node.value

    def remove(self, key):
        assert key in self, "Invalid map key."
        (self._root, tmp) = self._avlRemove(self._root, key)
        self._size -= 1

    def __iter__(self):
        return _BSTMapIterator(self._root)

    # Helper method that recursively searches the tree for a target key.
    def _bstSearch(self, subtree, target):
        if subtree is None :    # base case
            return None
        elif target < subtree.key: # target is left of  the subtree root.
            return self._bstSearch(subtree.left, target)
        elif target > subtree.key: # target is right of the subtree root.
            return self._bstSearch(subtree.right, target)
        else :                  # base case
            return subtree

    # Rotates the pivot to the right around its left child.
    def _avlRotateRight(self, pivot):
        C = pivot.left
        pivot.left = C.right
        C.right = pivot
        return C

    # Rotates the pivot to the left around its right child.
    def _avlRotateLeft(self, pivot):
        C = pivot.right
        pivot.right = C.left
        C.left = pivot
        return C

    # Rebalance a node when its left subtree is higher.
    def _avlLeftBalance(self, pivot):
        # Set L to point to the left child of the pivot.
        L = pivot.left
        C = pivot.left

        # See if the rebalancing is due to case 1.
        if C.bfactor == LEFT_HIGH :
            pivot.bfactor = EQUAL_HIGH
            C.bfactor = EQUAL_HIGH
            pivot = self._avlRotateRight(pivot)

        # Otherwise, a balance from the left is due to case 2.
        else :
            G = C.right

            # Change the balance factors.
            if G.bfactor == LEFT_HIGH :
                pivot.bfactor = RIGHT_HIGH
                C.bfactor = EQUAL_HIGH
            elif G.bfactor == EQUAL_HIGH:
                pivot.bfactor = EQUAL_HIGH
                C.bfactor = EQUAL_HIGH
            else :
                pivot.bfactor = EQUAL_HIGH
                C.bfactor = LEFT_HIGH

            # All three cases set G's balance factor to equal high.
            G.bfactor = EQUAL_HIGH

            # Perform the double rotation.
            pivot.left = self._avlRotateLeft(L)
            pivot = self._avlRotateRight(pivot)
        return pivot

    def _avlRightBalance(self, pivot):
        # Set L to point to the right child of the pivot.
        R = pivot.right
        C = pivot.right

        # See if the rebalancing is due to case 2.
        if C.bfactor == RIGHT_HIGH :
            pivot.bfactor = EQUAL_HIGH
            C.bfactor = EQUAL_HIGH
            pivot = self._avlRotateLeft(pivot)

        # Otherwise, a balance from the right is due to case 4.
        else :
            G = C.right

            # Change the balance factors.
            if G.bfactor == RIGHT_HIGH :
                pivot.bfactor = RIGHT_HIGH
                C.bfactor = EQUAL_HIGH
            elif G.bfactor == EQUAL_HIGH:
                pivot.bfactor = EQUAL_HIGH
                C.bfactor = EQUAL_HIGH
            else :
                pivot.bfactor = EQUAL_HIGH
                C.bfactor = RIGHT_HIGH

            # All three cases set G's balance factor to equal high.
            G.bfactor = EQUAL_HIGH

            # Perform the double rotation.
            pivot.right = self._avlRotateRight(R)
            pivot = self._avlRotateLeft(pivot)

        return pivot

    # Recursive method to handle the insertion into an AVL tree. The
    # function returns a tuple containing a reference to the root of the
    # subtree and a boolean to indicate if the subtree grew taller.
    def _avlInsert(self, subtree, key, newitem):
        # See if we have found the insertion point.
        if subtree is None :
            subtree = _AVLMapNode(key, newitem)
            taller = True

        # Is the key already in the tree?
        elif key == subtree.key:
            subtree.value = newitem
            return (subtree, False)

        # See if we need to navigate to the left.
        elif key < subtree.value:
            (subtree, taller) = self._avlInsert(subtree.left, key, newitem)

            # If the subtree grew taller, see if it needs rebalancing.
            if taller :
                if subtree.bfactor == LEFT_HIGH :
                    subtree.right = _avlLeftBalance(subtree)
                    taller = False
                elif subtree.bfactor == EQUAL_HIGH:
                    subtree.bfactor = LEFT_HIGH
                    taller = True
                else :
                    # RIGHT_HIGH
                    subtree.bfactor = EQUAL_HIGH
                    taller = False

        # Otherwise, navigate to the right.
        else :
            (node, taller) = self._avlInsert(subtree.right, key, newitem)

            # If the subtree grew taller, see if it needs rebalancing.
            if taller :
                if subtree.bfactor == LEFT_HIGH :
                    subtree.bfactor = EQUAL_HIGH
                    taller = False
                elif subtree.bfactor == EQUAL_HIGH:
                    subtree.bfactor = RIGHT_HIGH
                    taller = True
                else :
                    # RIGHT_HIGH
                    subtree.right = _avlRightBalance(subtree)
                    taller = False

        # Return the results.
        return (subtree, taller)

# Storage class for creating the AVL tree node.
class _AVLMapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.bfactor = EQUAL_HIGH
        self.left = None
        self.right = None

# An iterator for the binary search tree using a software stack.
class _BSTMapIterator:
    def __init__(self, root):
        self._theStack = Stack()
        self._traverseToMinnode(root)

    def __iter__(self):
        return self

    def __next__(self):
        if self._theStack.isEmpty() :
            raise StopIteration
        else :
            node = self._theStack.pop()
            key = node.key

            if node.right is not None :
                self._traverseToMinNode(node.right)

    def _traverseToMinNode(self, subtree):
        if subtree is not None :
            self._theStack.push(subtree)
            self._traverseToMinNode(subtree.left)

