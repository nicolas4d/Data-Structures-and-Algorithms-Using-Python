import unittest
from pyliststack import *

class TestStack(unittest.TestCase):
    def test_init(self):
        stk = Stack()
        self.assertEqual(len(stk), 0)

    def test_len(self):
        stk = Stack()
        self.assertEqual(len(stk), 0)
        stk.push(0)
        self.assertEqual(len(stk), 1)

    def test_isEmpty(self):
        stk = Stack()
        self.assertEqual(stk.isEmpty(), True)
        stk.push(0)
        self.assertEqual(stk.isEmpty(), False)

    def test_peek(self):
        stk = Stack()
        stk.push(0)
        self.assertEqual(stk.peek(), 0)

    def test_pop(self):
        stk = Stack()
        stk.push(0)
        self.assertEqual(stk.pop(), 0)

    def test_push(self):
        stk = Stack()
        stk.push(0)
        self.assertEqual(stk.pop(), 0)

if __name__ == '__main__':
    unittest.main()
