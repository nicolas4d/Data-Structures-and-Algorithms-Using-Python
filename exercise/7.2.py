from lliststack import Stack

values = Stack()

for i in range( 16 ) :
    if i % 3 == 0 :
        values.push( i )
    elif i % 4 == 0 :
        values.pop()

while not values.isEmpty():
    print(values.pop())
