# sample 1
# Fill a 1-D array with random values, then print them, one per line.

from array import Array
import random

# The constructor is called to create the array.
valueList = Array( 100 )

# Fill the array with random floating-point values.
for i in range( len( valueList ) ) :
    valueList[ i ] = random.random()

# Print the values, one per line.
for value in valueList :
    print( value )


# sample 2
#Count the number of occurrences of each letter in a text file.

# Create an array for the counters and initialize each element to 0.
theCounters = Array( 127 )
theCounters.clear( 0 )

# Open the text file for reading and extract each line from the file
# and iterate over each character in the line.
theFile = open( 'useArray.py', 'r' )
for line in theFile :
    for letter in line :
        code = ord( letter )
        theCounters[code] += 1
# Close the file
theFile.close()

# Print the results. The uppercase letters have ASCII values in the
# range 65..90 and the lowercase letters are in the range 97..122.
for i in range( 26 ) :
    print( "%c - %4d        %c - %4d" % \
           (chr(65+i), theCounters[65+i], chr(97+i), theCounters[97+i]) )
