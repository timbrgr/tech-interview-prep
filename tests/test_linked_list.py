import unittest

from datastructures.linkedlist import SinglyLinkedList, DoublyLinkedList


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

        for current_node, i in zip(sll.next_node_start_from_head(), [1, 3]):
            self.assertEqual(current_node.data, i)

    def testRemoveNonExisting(self):
        sll = self.get_test_sll()
        sll.remove(99)
        self.assertEqual(sll.size, 3)


class TestDoublyLinkedList(unittest.TestCase):

    @staticmethod
    def get_test_dll() -> DoublyLinkedList:
        dll = DoublyLinkedList()
        dll.insert(1)
        dll.insert(2)
        dll.insert(3)

        return dll

    def testSize(self):
        dll = self.get_test_dll()
        actual = dll.size
        self.assertEqual(actual, 3)

    def testTail(self):
        dll = self.get_test_dll()
        actual = dll.tail
        self.assertEqual(actual.data, 3)

    def testPrev(self):
        dll = self.get_test_dll()
        actual = dll.tail.prev
        self.assertEqual(actual.data, 2)

    def testRemove(self):
        dll = self.get_test_dll()
        dll.remove(2)

        for current_node, i in zip(dll.next_node_start_from_head(), [1, 3]):
            self.assertEqual(current_node.data, i)

    def testRemoveNonExisting(self):
        dll = self.get_test_dll()
        dll.remove(99)
        self.assertEqual(dll.size, 3)
