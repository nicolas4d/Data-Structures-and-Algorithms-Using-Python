def printInorder( node ):
    if node is not None :
        print( node.data )
        printInorder( node.next )
