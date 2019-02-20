import unittest

from datastructures.stack import Stack


class TestStack(unittest.TestCase):
    """Test cases for the stack.
    """

    @staticmethod
    def get_test_stack():
        stack = Stack()
        stack.push(5)
        stack.push(6)

        return stack

    def testOnEmpty(self):
        empty_stack = Stack()
        self.assertRaises(IndexError, empty_stack.pop)

    def testPeek(self):
        stack = self.get_test_stack()
        self.assertEqual(6, stack.peek())

    def testPush(self):
        stack = self.get_test_stack()
        stack.push(7)
        self.assertEqual(7, stack.peek())

    def testPop(self):
        stack = self.get_test_stack()
        self.assertEqual(6, stack.pop())

    def testSize(self):
        stack = self.get_test_stack()
        self.assertEqual(2, stack.size())

    def testIsEmpty(self):
        empty_stack = Stack()
        self.assertTrue(empty_stack.is_empty())

        stack = self.get_test_stack()
        self.assertFalse(stack.is_empty())