from life import LifeGrid

# INIT_CONFIG = [(1, 1), (1, 2), (2, 2), (3, 2)]

# exercise 2.5
# size as 5 , generation as 11
# INIT_CONFIG = [(3, 1), (2, 2), (1, 3)]

# exercise 2.5
# size as 5 , generation as 11
INIT_CONFIG = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), \
               (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), \
               (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), \
               (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), \
               (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]

GRID_WIDTH = 5
GRID_HEIGHT = 5

NUM_GENS = 8

# exercise 2.3
def prompt():
    print("please input the size: ")

    global GRID_WIDTH
    global GRID_HEIGHT
    GRID_WIDTH = int(input())
    GRID_HEIGHT = GRID_WIDTH

    print("please input the generation: ")

    global NUM_GENS
    NUM_GENS = int(input())

def main():

    prompt()

    grid = LifeGrid(GRID_WIDTH, GRID_HEIGHT)
    grid.configure(INIT_CONFIG)

    draw(grid)
    for i in range(NUM_GENS):
        evolve(grid)
        draw(grid)

def evolve(grid):
    liveCells = list()

    for i in range(grid.numRows()) :
        for j in range(grid.numCols()):
            neighbors = grid.numLiveNeighbors(i, j)

            if (neighbors == 2 and grid.isLiveCell(i, j)) or \
               (neighbors == 3) :
                liveCells.append((i, j))

    grid.configure(liveCells)

def draw(grid):
    for r in range(grid.numRows()):
        for c in range(grid.numCols()):
            if grid.isLiveCell(r, c):
                print("@ ", end="")
            else:
                print(". ", end="")
        print()
main()
