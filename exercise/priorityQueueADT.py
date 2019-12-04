from bpriorityq import BPriorityQueue

q = BPriorityQueue(6)
q.enqueue( "purple", 5)
q.enqueue("black", 1)
q.enqueue("orange", 3)
q.enqueue("white", 0)
q.enqueue("green", 1)
q.enqueue("yellow", 5)

while not q.isEmpty():
    item = q.dequeue()
    print(item)

