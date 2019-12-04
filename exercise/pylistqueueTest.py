import unittest
from pylistqueue import *

class TestQueue(unittest.TestCase):
    def test_init(self):
        q = Queue()

    def test_len(self):
        q = Queue()
        self.assertEqual(len(q), 0)
        q.enqueue(1)
        self.assertEqual(len(q), 1)

    def test_isEmpty(self):
        q = Queue()
        self.assertEqual(q.isEmpty(), True)
        q.enqueue(q)
        self.assertEqual(q.isEmpty(), False)

    def test_enqueue(self):
        q = Queue()
        q.enqueue(1)
        self.assertEqual(len(q), 1)

    def test_dequeue(self):
        q = Queue()
        q.enqueue(1)
        self.assertEqual(q.dequeue(), 1)

    def test_reverse(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.reverse()
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 1)

if __name__ == '__main__':
    unittest.main()
