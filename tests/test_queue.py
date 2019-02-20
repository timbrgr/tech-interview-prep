import unittest

from datastructures.queue import Queue


class TestQueue(unittest.TestCase):
    """Test cases for the Queue.
    """

    @staticmethod
    def get_test_queue():
        stack = Queue()
        stack.add(5)
        stack.add(6)

        return stack

    def testOnEmpty(self):
        empty_queue = Queue()
        self.assertRaises(IndexError, empty_queue.remove)

    def testPeek(self):
        queue = self.get_test_queue()
        self.assertEqual(5, queue.peek())

    def testAdd(self):
        queue = self.get_test_queue()
        queue.add(7)
        self.assertEqual(7, queue.items[-1])

    def testRemove(self):
        queue = self.get_test_queue()
        queue.remove()
        self.assertEqual(6, queue.peek())

    def testSize(self):
        queue = self.get_test_queue()
        self.assertEqual(2, queue.size())

    def testIsEmpty(self):
        empty_queue = Queue()
        self.assertTrue(empty_queue.is_empty())

        queue = self.get_test_queue()
        self.assertFalse(queue.is_empty())