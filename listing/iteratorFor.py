# Create a BagIterator object for myBag.
iterator = myBag.__iter__()

# Repeat the while loop until break is called.
while True :
    try:
        # Get the next item from the bag. If there are no
        # more items, the StopIteration exception is raised.
        item = iterator.__next__()
        # Perform the body of the for loop.
        print( item )
        
    # Catch the exception and break from the loop when we are done.
    except StopIteration:
            break
