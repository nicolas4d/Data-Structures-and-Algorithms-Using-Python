from life import LifeGrid
import unittest

class LifeGridTest(unittest.TestCase):
    def test__init__(self):
        lifegrid = LifeGrid(5, 5)
        self.assertEqual(LifeGrid.DEAD_CELL, 0)
        self.assertEqual(lifegrid.LIVE_CELL, 1)

    def test_numRows(self):
        lifegrid = LifeGrid(5, 5)
        self.assertEqual(lifegrid.numRows(), 5)

    def test_numCols(self):
        lifegrid = LifeGrid(5, 5)
        self.assertEqual(lifegrid.numCols(), 5)

    def test_configure(self):
        lifegrid = LifeGrid(5, 5)
        lifegrid.configure([(0, 0)])
        self.assertEqual(lifegrid.isLiveCell(0, 0), True)

    def test_isLiveCell(self):
        # check test_configure
        pass

    def test_clearCell(self):
        lifegrid = LifeGrid(5, 5)
        lifegrid.configure([(0, 0)])
        self.assertEqual(lifegrid.isLiveCell(0, 0), True)
        lifegrid.clearCell(0, 0)
        self.assertEqual(lifegrid.isLiveCell(0, 0), False)

    def test_setCell(self):
        lg = LifeGrid(5, 5)
        lg.setCell(0, 0)
        self.assertEqual(lg.isLiveCell(0, 0), True)

    def test_numLiveNeighbors(self):
        lifegrid = LifeGrid(5, 5)
        lifegrid.configure([(1, 1)])
        self.assertEqual(lifegrid.numLiveNeighbors(1, 1), 0)
        self.assertEqual(lifegrid.numLiveNeighbors(0, 0), 1)
        self.assertEqual(lifegrid.numLiveNeighbors(3, 3), 0)

        lifegrid.setCell(0,0)
        self.assertEqual(lifegrid.numLiveNeighbors(0, 1), 2)

unittest.main()
