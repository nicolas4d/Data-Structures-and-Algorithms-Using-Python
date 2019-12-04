# Print the moves required to solve the Towers of Hanoi puzzle.
# O(2^n)
def move(n, src, dest, temp):
    if n >= 1:
        move(n - 1, src, temp, dest)
        print("Move %d -> %d" % (src, dest))
        move(n - 1, temp, dest, src)

move(5, 1, 3, 2)


