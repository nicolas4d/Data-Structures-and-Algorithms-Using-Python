from lliststack import Stack

values = Stack()
for i in range( 16 ) :
    if i % 3 == 0 :
        values.push( i )

while not values.isEmpty():
    print(values.pop())
