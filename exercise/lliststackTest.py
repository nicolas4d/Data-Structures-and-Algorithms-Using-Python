import unittest
from lliststack import *

class TestStack(unittest.TestCase):
    def test_init(self):
        s = Stack()
        self.assertEqual(s._size, 0)

    def test_isEmpty(self):
        s = Stack()
        self.assertEqual(s.isEmpty(), True)
        s.push(0)
        self.assertEqual(s.isEmpty(), False)

    def test_len(self):
        s = Stack()
        self.assertEqual(len(s), 0)
        s.push(0)
        self.assertEqual(len(s), 1)

    def test_peek(self):
        s = Stack()
        s.push(0)
        self.assertEqual(s.peek(), 0)

    def test_pop(self):
        s = Stack()
        s.push(0)
        self.assertEqual(s.pop(), 0)

    def test_push(self):
        s = Stack()
        s.push(0)
        self.assertEqual(s.pop(), 0)

if __name__ == '__main__':
    unittest.main()
