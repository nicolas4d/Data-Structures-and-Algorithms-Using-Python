# Postorder traversal on a binary tree.
def postorderTrav( subtree ):
    if subtree is not None :
        postorderTrav( subtree.left )
        postorderTrav( subtree.right )
        print( subtree.data )
