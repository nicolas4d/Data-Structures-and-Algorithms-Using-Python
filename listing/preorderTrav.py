# Preorder traversal on a binary tree.
def preorderTrav( subtree ):
    if subtree is not None :
        print( subtree.data )
        preorderTrav( subtree.left )
        preorderTrav( subtree.right )
