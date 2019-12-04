def revTraversal( tail ):
    curNode = tail
    while curNode is not None :
        print( curNode.data )
        curNode = curNode.prev
