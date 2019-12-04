def searchCircularList( listRef, target ):
    curNode = listRef
    done = listRef is None

    while not done :
        curNode = curNode.next
        if curNode.data == target :
            return True
        else :
            done = curNode is listRef or curNode.data > target
            
    return False
