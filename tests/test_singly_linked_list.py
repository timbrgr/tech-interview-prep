import unittest

from datastructures.linkedlist import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):

    @staticmethod
    def get_test_sll() -> SinglyLinkedList:
        sll = SinglyLinkedList()
        sll.insert(1)
        sll.insert(2)
        sll.insert(3)

        return sll

    def testSize(self):
        sll = self.get_test_sll()
        actual = sll.size
        self.assertEqual(actual, 3)

    def testSizeIn_O_n(self):
        sll = self.get_test_sll()
        actual = sll.size_O_n()
        self.assertEqual(actual, 3)

    def testSizeEmtpy(self):
        empty_sll = SinglyLinkedList()
        actual = 0
        self.assertEqual(actual, empty_sll.size)

    def testTail(self):
        sll = self.get_test_sll()
        actual = sll.tail
        self.assertEqual(actual.data, 3)

    def testTail_O_n(self):
        sll = self.get_test_sll()
        actual = sll.get_tail_O_n()
        self.assertEqual(actual.data, 3)

    def testRemove(self):
        sll = self.get_test_sll()
        sll.remove(2)
        self.assertEqual(sll.size, 2)


