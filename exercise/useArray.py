# sample 1
from array import Array
import random

valueList = Array(100)

for i in range(len(valueList)):
    valueList[i] = random.random()

for value in valueList:
    print(value)


# sample 2
theCounters = Array(127)
theCounters.clear(0)

theFile = open('testCytype.py', 'r')
for line in theFile:
    for letter in line:
        code = ord(letter)
        print(code)
        theCounters[code] += 1
theFile.close()

for i in range(26):
    print("%c - %4d     %c - %4d" % \
          (chr(65+i), theCounters[65+i], chr(97+i), theCounters[97+i]))
