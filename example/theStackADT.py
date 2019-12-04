PROMPT = "Enter an int value (<0 to end):"
myStack = Stack()
value = int(input( PROMPT ))
while value >= 0 :
    myStack.push( value )
    value = int(input( PROMPT ))
while not myStack.isEmpty() :
    value = myStack.pop()
    print( value )

# input 7 13 45 19 28 -1
