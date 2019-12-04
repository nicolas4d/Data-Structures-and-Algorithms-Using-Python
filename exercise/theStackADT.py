from pyliststack import Stack

PROMPT = "Enter and int value (<0 to ending:)"

myStack = Stack()
value = int(input(PROMPT))

while value >=0 :
    myStack.push(value)
    value = int(input(PROMPT))

while not myStack.isEmpty():
    value = myStack.pop()
    print(value)

# input 7 13 45 19 28 -1
