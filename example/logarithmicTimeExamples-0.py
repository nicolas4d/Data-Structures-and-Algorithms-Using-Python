def ex7( n ):
    count = 0
    for i in range( n ) :
        count += ex6( n )
    return count
