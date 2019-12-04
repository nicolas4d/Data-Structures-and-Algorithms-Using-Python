import unittest
from arrayqueue import *

class TestQueue(unittest.TestCase):
    def test_init(self):
        q = Queue(4)

    def test_isEmpty(self):
        q = Queue(4)
        self.assertEqual(q.isEmpty(), True)
        q.enqueue(1)
        self.assertEqual(q.isEmpty(), False)

    def test_isFull(self):
        q = Queue(1)
        self.assertEqual(q.isFull(), False)
        q.enqueue(1)
        self.assertEqual(q.isFull(), True)

    def test_len(self):
        q = Queue(4)
        self.assertEqual(len(q), 0)
        q.enqueue(1)
        self.assertEqual(len(q), 1)

    def test_enqueue(self):
        q = Queue(4)
        q.enqueue(1)
        self.assertEqual(len(q), 1)

    def test_dequeue(self):
        q = Queue(4)
        q.enqueue(1)
        self.assertEqual(q.dequeue(), 1)

if __name__ == '__main__':
    unittest.main()
