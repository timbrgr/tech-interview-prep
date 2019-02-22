import unittest

from datastructures.singlylinkedlist import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):

    @staticmethod
    def get_test_sll() -> SinglyLinkedList:
        sll = SinglyLinkedList()
        sll.insert(1)
        sll.insert(2)
        sll.insert(3)

        return sll

    def testTail(self):
        sll = self.get_test_sll()
        actual = sll.get_tail()
        self.assertEqual(actual.data, 3)

    def testRemove(self):
        sll = self.get_test_sll()
        sll.remove(2)
        self.assertEqual(sll.get_tail().data, 3)
        self.assertEqual(sll.size(), 2)

    def testSize(self):
        sll = self.get_test_sll()
        actual = sll.size()
        self.assertEqual(actual, 3)

    def testSizeEmtpy(self):
        empty_sll = SinglyLinkedList()
        actual = 0
        self.assertEqual(actual, empty_sll.size())
