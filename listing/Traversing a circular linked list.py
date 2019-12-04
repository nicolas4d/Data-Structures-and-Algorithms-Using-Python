def traverse( listRef ):
    curNode = listRef
    done = listRef is None
    while not done :
        curNode = curNode.next
        print curNode.data
        done = curNode is listRef
