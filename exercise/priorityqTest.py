import unittest
from priorityq import *
from priorityq import _PriorityQEntry

class TestPriority(unittest.TestCase):
    def test_init(self):
        pq = PriorityQueue()

    def test_len(self):
        pq = PriorityQueue()
        self.assertEqual(len(pq), 0)
        pq.enqueue(1, 2)
        self.assertEqual(len(pq), 1)

    def test_isEmpty(self):
        pq = PriorityQueue()
        self.assertEqual(pq.isEmpty(), True)
        pq.enqueue(1, 1)
        self.assertEqual(pq.isEmpty(), False)

    def test_enqueue(self):
        pq = PriorityQueue()
        pq.enqueue(1, 1)
        self.assertEqual(len(pq), 1)

    def test_dequeue(self):
        pq = PriorityQueue()
        pq.enqueue(1, 1)
        pq.enqueue(0, 0)
        self.assertEqual(pq.dequeue(), 0)


class Test_PriorityQEntry(unittest.TestCase):
    def test_init(self):
        pqe = _PriorityQEntry("item", 0)

if __name__ == '__main__':
    unittest.main()
