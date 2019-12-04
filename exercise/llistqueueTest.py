import unittest
from llistqueue import *
from llistqueue import _QueueNode

class TestQueue(unittest.TestCase):
    def test_init(self):
        q = Queue()

    def test_isEmpty(self):
        q = Queue()
        self.assertEqual(q.isEmpty(), True)
        q.enqueue(1)
        self.assertEqual(q.isEmpty(), False)

    def test_len(self):
        q = Queue()
        self.assertEqual(len(q), 0)
        q.enqueue(1)
        self.assertEqual(len(q), 1)

    def test_enqueue(self):
        q = Queue()
        q.enqueue(1)
        self.assertEqual(len(q), 1)

    def test_dequeue(self):
        q = Queue()
        q.enqueue(1)
        self.assertEqual(q.dequeue(), 1)

class _QueueNodeTest(unittest.TestCase):
    def test_init(self):
        qnode = _QueueNode(1)

if __name__ == '__main__':
    unittest.main()
