from llistqueue import Queue

values = Queue()
for i in range( 16 ) :
    if i % 3 == 0 :
        values.enqueue( i )
    elif i % 4 == 0 :
        values.dequeue()

while not values.isEmpty():
    print(values.dequeue())
