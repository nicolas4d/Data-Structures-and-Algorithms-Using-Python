# Given a head and tail reference and a new value, add the new value to a
# sorted doubly linked list.
newnode = DListNode( value )

if head is None :
    # empty list
    head = newnode
    tail = head
elif value < head.data : # insert before head
    newnode.next = head
    head.prev = newnode
    head = newnode
elif value > tail.data : # insert after tail
    newnode.prev = tail
    tail.next = newnode
    tail = newnode
else : # insert in the middle
node = head
while node is not None and node.data < value :
    node = node.next

newnode.next = node
newnode.prev = node.prev
node.prev.next = newnode
node.prev = newnode
