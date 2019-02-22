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
        """Adds an element to the end of the list."""
        new_node = LinkedListNode(data)
        if not self.head:  # list is empty, head will be new node
            self.head = new_node
            return

        # traverse the list from head to tail, add new element to tail
        tail = self.get_tail()
        tail.next = new_node

    def get_tail(self) -> LinkedListNode:
        """Returns the tail (last element in list) by traversing through it. O(n)."""
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        return current_node

    def remove(self, data: T) -> None:
        """Removes the node and updates pointers. Assumes unique values in data."""
        if self.head and self.head.data == data:
            self.head = None
            return

        prev_node = self.head
        for current_node in self.next_node():
            if not current_node.next:  # reached tail
                prev_node.next = None
                return

            if current_node.data == data:
                prev_node.next = current_node.next
                return
            prev_node = current_node

    def next_node(self):
        """Returns the next node. Starts with head."""
        yield self.head
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
            yield current_node

    def size(self) -> int:
        """Returns the number of nodes."""
        if not self.head:
            return 0
        else:
            return sum(1 for node in self.next_node())
