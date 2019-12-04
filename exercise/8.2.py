from llistqueue import Queue

values = Queue()
for i in range( 16 ) :
    if i % 3 == 0 :
        values.enqueue( i )

while not values.isEmpty():
    print(values.dequeue())
