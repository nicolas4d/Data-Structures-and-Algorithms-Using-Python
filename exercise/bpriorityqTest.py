import unittest
from bpriorityq import *

class TestBPriorityQueue(unittest.TestCase):
    def test_init(self):
        bpq = BPriorityQueue(4)

    def test_len(self):
        bpq = BPriorityQueue(4)
        self.assertEqual(len(bpq), 0)
        bpq.enqueue(0, 0)
        self.assertEqual(len(bpq), 1)

    def test_isEmpty(self):
        bpq = BPriorityQueue(4)
        self.assertEqual(bpq.isEmpty(), True)
        bpq.enqueue(0, 0)
        self.assertEqual(bpq.isEmpty(), False)

    def test_enqueue(self):
        bpq = BPriorityQueue(4)
        bpq.enqueue(0, 0)
        bpq.enqueue(1, 0)
        self.assertEqual(len(bpq), 2)

    def test_dequeue(self):
        bpq = BPriorityQueue(4)
        bpq.enqueue(1, 1)
        bpq.enqueue(0, 0)
        self.assertEqual(bpq.dequeue(), 0)

if __name__ == '__main__':
    unittest.main()
