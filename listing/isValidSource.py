# Implementation of the algorithm for validating balanced brackets in
# a C++ source file.
from lliststack import Stack

def isValidSource( srcfile ):
    s = Stack()
    for line in srcfile :
        print(line)
        for token in line :
            print(token)
            if token in "{[(" :
                s.push( token )
            elif token in "}])" :
                if s.isEmpty() :
                    return False
                else :
                    left = s.pop()
                    if (token == "}" and left != "{") or \
                       (token == "]" and left != "[") or \
                       (token == ")" and left != "(") :
                        return False

    return s.isEmpty()

