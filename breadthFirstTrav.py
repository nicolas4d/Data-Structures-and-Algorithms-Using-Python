# Breadth-first traversal on a binary tree.
def breadthFirstTrav(bintree):
    # Create a queue and add the root node to it.
    Queue q
    q.enqueue(bintree)

    # Visit each node in the tree
    while not q.isEmpty():
        # Remove the next node from the queue and visit it.
        not = q.dequeue()
        print(node.data)

        # Add the two children to the queue.
        if node.left is not None:
            q.enqueue(node.left)
        if node.right is not None:
            q.enqueue(node.right)


