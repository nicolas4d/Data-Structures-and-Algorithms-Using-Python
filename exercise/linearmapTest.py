from linearmap import Map
import unittest

class MapTest(unittest.TestCase):
    map = Map()

    def test__init__(self):
        map = Map()

    def test_len(self):
        self.assertEqual(len(self.map), 0)

    def test_add(self):
        map = Map()
        map.add(1,1)
        self.assertEqual(len(map), 1)

    def test__findPosition(self):
        map = Map()
        map.add(1, 1)
        self.assertEqual(map._findPosition(1), 0)

    def test_contains(self):
        map = Map()
        map.add(1, 1)
        self.assertEqual(map.__contains__(1), True)

    def test_valueOf(self):
        map = Map()
        map.add(1, 1)
        self.assertEqual(map.valueOf(1), 1)

    def test_remove(self):
        map = Map()
        map.add(1, 1)
        self.assertEqual(map.valueOf(1), 1)
        map.remove(1)

    def test_iter(self):
        map = Map()
        map.add(1, 1)
        map.add(2, 2)

        print()
        for entry in map:
            print(entry)

        print("iterator succeed")

unittest.main()
