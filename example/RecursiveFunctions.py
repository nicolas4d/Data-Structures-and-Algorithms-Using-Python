def printRev( n ):
    if n > 0 :
        print( n )
        printRev( n-1 )

printRev( 4 )

print()

def printInc( n ):
    if n > 0 :
        printInc( n-1 )
        print( n )

printInc(4)
