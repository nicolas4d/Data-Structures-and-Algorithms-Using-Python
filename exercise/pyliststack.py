# Implementation of the stack ADT using a python list.
class Stack:
    # Creates an empty stack.
    def __init__(self):
        self._theItems = list()

    # Returns the number of items in the stack.
    # O(1)
    def __len__(self):
        return len(self._theItems)

    # Return True if the stack is empty or False otherwise.
    # O(1)
    def isEmpty(self):
        return len(self) == 0

    # Returns the top iterm on the stack without removing it.
    # O(1)
    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack."
        return self._theItems[-1]

    # Removes and returns the top item on the stack.
    # O(n)
    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack."
        return self._theItems.pop()

    # Push an item onto the top of the stack.
    # O(n)
    def push(self, item):
        self._theItems.append(item)



