class Tree23Map :
    # ...
    def _23Search( subtree, target ):
        # If we encounter a null pointer, the target is not in the tree.
        if subtree is None :
            return None
        # See if the node contains the key. If so, return the data.
        elif subtree.hashKey( target ) :
            return subtree.getData( target )
        # Otherwise, take the appropriate branch.
        else :
            branch = subtree.getBranch( target )
            return _23Search( branch, target )

    def _23Insert( self, key, newitem ):
        # If the tree is empty, a node has to be created for the first key.
        if self._root is None :
            self._root = _23TreeNode( key, newitem )
            # Otherwise, find the correct leaf and insert the key.
        else :
            (pKey, pData, pref) = self._23RecInsert( self._root, key, newitem )

            # See if the node was split.
            if pKey is not None :
                newRoot = _23TreeNode( pKey, pData )
                newRoot.left = self._root
                newRoot.middle = pRef
                self._root = newRoot

    # Recursive function to insert a new key into the tree.
    def _23RecInsert( subtree, key, newitem ):
        # Make sure the key is not already in the tree.
        if subtree.hasKey( key ) :
            return (None, None, None)

        # Is this a leaf node?
        elif subtree.isALeaf() :
            return _23AddToNode( subtree, key, newitem, None )

        # Otherwise, it's an interior node.
        else :
            # Which branch do we take?
            branch = subtree.getBranch( key )
            (pKey, pData, pRef) = self._23RecInsert( branch, key, newitem )

            # If the child was split, the promoted key and reference have to be
            # added to the interior node.
            if pKey is None :
                return (None, None, None)
            else :
                return _23AddToNode( subtree, pKey, pData, pRef )

    def _23AddToNode( self, subtree, key, data, pRef ):
        # If the leaf is full, it has to be split.
        if subtree.isFull() :
            return self._23SplitNode( subtree, key, data, None )
        # Otherwise, add the new key in its proper order.
        else :
            if key < subtree.key1 :
                subtree.key2 = subtree.key1
                subtree.data2 = subtree.data1
                subtree.key1 = key
                subtree.data1 = data
                if pRef is not None : # If interior node, set the links.
                    subtree.right = subtree.middle
                    subtree.middle = pRef
            else :
                subtree.key2 = key
                subtree.data2 = data
                if pRef is not None : # If interior node, set the links.
                    subtree.right = pRef

            return (None, None, None)

    # If pRef != None, then an interior node is being split so the new
    # node N created in the function will also be an interior node. In that
    # case, the links of the interior node have to be set appropriately.
    def _23SplitNode( self, node, key, data, pRef ):
        # Create the new node, the reference to which will be promoted.
        newnode = _23TreeNode( None, None )
        # See where the key belongs.
        if key < node.key1 :
            # left
            pKey = node.key1
            pData = node.data1
            node.key1 = key
            node.data1 = data
            newnode.key1 = node.key2
            newnode.data1 = node.data2
            if pRef is not None : # If interior node, set its links.
                newnode.left = node.middle
                newnode.middle = node.right
                node.middle = pRef
        elif key < node.key2 :
            # middle
            pKey = key
            pData = data
            newnode.key1 = node.key2
            newnode.data1 = node.data2
            if pRef is not None : # If interior node, set its links.
                newnode.left = pRef
                newnode.middle = node.right
        else :
            # right
            pKey = node.key2
            pData = node.data2
            newnode.key1 = key
            newnode.data1 = data
            if pRef is not None : # If interior node, set its links.
                newnode.left = node.right
                newnode.middle = pRef

        # The second key of the original node has to be set to null.
        node.key2 = None
        node.data2 = None
        # Return the promoted key and reference to the new node.
        return (pKey, pData, newnode)

class _23TreeNode( object ):
    def __init__( self, key, data ):
        self.key1 = key
        self.key2 = None
        self.data1 = data
        self.data2 = None
        self.left = None
        self.middle = None
        self.right = None

    # Is this a leaf node?
    def isALeaf( self ):
        return self.left is None and self.middle is None and self.right is None

    # Are there two keys in this node?
    def isFull( self ):
        return self.key2 is not None

    # Does the node contain the given target key?
    def hasKey( self, target ):
        if (target == self.key1) or \
           (self.key2 is not None and target == self.key2) :
            return True
        else :
            return False

    # Returns the data associated with the target key or None.
    def getData( self, target ):
        if target == self.key1 :
            return self.data1
        elif self.key2 is not None and target == self.key2 :
            return self.data2
        else :
            return None

    # Chooses the appropriate branch for the given target.
    def getBranch( self, target ):
        if target < self.key1 :
            return self.left
        elif self.key2 is None :
            return self.middle
        elif target < self.key2 :
            return self.middle
        else :
            return self.right
