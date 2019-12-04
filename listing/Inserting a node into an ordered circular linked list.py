# Given a listRef pointer and a value, add the new value
# to an ordered circular linked list.
newnode = ListNode( value )

if listRef is None :    # empty list
    listRef = newNode
    newNode.next = newNode
elif value < listRef.next.data : # insert in front
    newNode.next = listRef.next
    listRef.next = newNode
elif value > listRef.data :    # insert in back
    newNode.next = listRef.next
    listRef.next = newNode
    listRef = newNode
else :    # insert in the middle
    # Position the two pointers.
    predNode= None
    curNode = listRef
    done = listRef is None
    while not done :
        predNode = curNode
        predNode = curNode.next
        done = curNode is listRef or curNode.data > target

    # Adjust links to insert the node.
    newNode.next = curNode
    predNode.next = newNode
