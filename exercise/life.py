from array import Array2D

class LifeGrid:
    # Defines constants to represent the cell states.
    DEAD_CELL = 0
    LIVE_CELL = 1

    def __init__(self, numRows, numCols):
        "create"
        self._grid = Array2D(numRows, numCols)
        self.configure(list())

    def numRows(self):
        return self._grid.numRows()

    def numCols(self):
        return self._grid.numCols()

    def configure(self, coordList):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                self.clearCell(r, c)

        for coord in coordList :
            self.setCell(coord[0], coord[1])

    def isLiveCell(self, row, col):
        return self._grid[row, col] == LifeGrid.LIVE_CELL

    def clearCell(self, row, col):
        self._grid[row, col] = LifeGrid.DEAD_CELL

    def setCell(self, row, col):
        self._grid[row, col] = LifeGrid.LIVE_CELL

    def numLiveNeighbors(self, row, col):
        numLinveNeighbors = 0

        for r in [row - 1, row, row + 1]:
            for c in [col - 1, col, col + 1]:
                # overflow of grid is continue
                if r < 0 or r >= self.numRows() or \
                   c < 0 or c >= self.numCols() :
                    continue
                # continue (row, col)
                elif (r == row and c == col) :
                    continue
                # plus 1 neighbors if live
                elif self.isLiveCell(r, c) :
                    numLinveNeighbors += 1

        return numLinveNeighbors
