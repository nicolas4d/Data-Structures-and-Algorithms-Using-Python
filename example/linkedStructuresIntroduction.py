class ListNode :
    def __init__( self, data ) :
        self.data = data

a = ListNode( 11 )
b = ListNode( 52 )
c = ListNode( 18 )

class ListNode :
    def __init__( self, data ) :
        self.data = data
        self.next = None

a.next = b
b.next = c

a = None
b= None

print( a.data )
print( a.next.data )
print( a.next.next.data )
