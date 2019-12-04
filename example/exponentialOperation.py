# O(n)
def exp1( x, n ):
    y = 1
    for i in range( n ):
        y *= x
    return y
