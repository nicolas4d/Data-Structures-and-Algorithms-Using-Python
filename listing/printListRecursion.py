# Print the contents of a linked list using recursion.
# O(n)
def printList( node ):
    if node is not None :
        printList( node.next )
        print( node.data )
