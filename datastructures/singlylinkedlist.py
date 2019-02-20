from typing import TypeVar

from datastructures.linkedlistnode import LinkedListNode


class SinglyLinkedList:
    """Implements a generic singly linked list.
    Each element has a pointer to the next node in the list. The last elements points to None.
    """

    T = TypeVar('T')

    def __init__(self):
        self.head = None

    def insert(self, data: T) -> None:
        """Adds an element to the end of the list.
        """
        new_node = LinkedListNode(data)
        if not self.head:  # list is empty, head will be new node
            self.head = new_node
            return

        tail = self.get_tail()  # traverse the list from head till tail, add new element to tail
        tail.next = new_node

    def get_tail(self) -> LinkedListNode:
        """Returns the tail (last element in list) by traversing through it. O(n).
        """
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        return current_node

    def next_node(self):
        current_node = self.head
        while current_node.next:
            yield current_node.next

    def size(self) -> int:
        for i, yielded in enumerate(self.next_node()):
            if not yielded:
                i = 0
        return i
