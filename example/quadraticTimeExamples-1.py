def ex5( n ):
    count = 0
    for i in range( n ) :
        for j in range( i+1 ) :
            count += 1
    return count
