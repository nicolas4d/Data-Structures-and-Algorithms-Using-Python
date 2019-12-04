# Print the moves required to solve the Towers of Hanoi puzzle.
# O(2^n)
def move( n, src, dest, temp ):
    if n >= 1 :
        move( n - 1, src, temp, dest )
        print( "Move %d -> %d" % (src, dest))
        move( n - 1, temp, dest, src )

move( 3, 1, 3, 2 )
"""
Move 1 -> 3
Move 1 -> 2
Move 3 -> 2
Move 1 -> 3
Move 2 -> 1
Move 2 -> 3
Move 1 -> 3
"""

print()
move( 5, 1, 3, 2 )
