import unittest
from llistMergeSort import *
from llistMergeSort import _splitLinkedList
from llistMergeSort import _mergeLinkedLists

class TestllistMergeSort(unittest.TestCase):
    def test__splitLinkedList(self):
        a = ListNode(4)
        b = ListNode(3)
        c = ListNode(5)
        d = ListNode(1)

        a.next = b
        b.next = c
        c.next = d

        rightList = _splitLinkedList(a)
        self.assertEqual(rightList.data, 5)

    def test_mergeLinkedLists(self):
        a = ListNode(4)
        b = ListNode(2)

        newList = _mergeLinkedLists(a, b)
        self.assertEqual(newList.data, 2)

    def test_llistMergeSort(self):
        a = ListNode(4)
        b = ListNode(3)
        c = ListNode(5)
        d = ListNode(1)

        a.next = b
        b.next = c
        c.next = d

        newList = llistMergeSort(a)

        self.assertEqual(newList.data, 1)
        self.assertEqual(newList.next.data, 3)
        self.assertEqual(newList.next.next.data, 4)
        self.assertEqual(newList.next.next.next.data, 5)

if __name__ == '__main__':
    unittest.main()
