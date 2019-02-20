import unittest

from datastructures.linkedlistnode import LinkedListNode
from datastructures.singlylinkedlist import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):

    @staticmethod
    def get_test_sll() -> SinglyLinkedList:
        sll = SinglyLinkedList()
        sll.insert(LinkedListNode(1))
        sll.insert(LinkedListNode(2))

        return sll

    def testAdd(self):
        sll = SinglyLinkedList()
        sll.insert(LinkedListNode(1))
        sll.insert(LinkedListNode(2))
        raise NotImplementedError()

    def testTail(self):
        sll = self.get_test_sll()
        actual = sll.get_tail().data
        self.assertEqual(actual, 2)

    def testSize(self):
        sll = self.get_test_sll()
        actual = sll.size()
        self.assertEqual(actual, 2)


