def sortedSearch( head, target ) :
    curNode = head
    
    while curNode is not None and curNode.data < target :
        if curNode.data == target :
            return True
        else :
            curNode = node.next

    return False
