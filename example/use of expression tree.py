# Create a dictionary containing values for the one-letter variables.
vars = { 'a' : 5, 'b' : 12 }

# Build the tree for a sample expression and then evaluate it.
expTree = expressionTree( "(a/(b-3))" )
print( "The result = ", expTree.evaluate(vars) )

# We can change the value assigned to a variable and reevaluate.
vars['a'] = 22
print( "The result = ", expTree.evaluate(vars) )
