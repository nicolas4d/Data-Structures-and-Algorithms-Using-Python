totalSum = 0
# Version 1
for i in range( n ) :
    rowSum[i] = 0
    for j in range( n ) :
        rowSum[i] = rowSum[i] + matrix[i,j]
        totalSum = totalSum + matrix[i,j]















totalSum = 0
# Version 2
for i in range( n ) :
    rowSum[i] = 0
    for j in range( n ) :
        rowSum[i] = rowSum[i] + matrix[i,j]
    totalSum = totalSum + rowSum[i]
