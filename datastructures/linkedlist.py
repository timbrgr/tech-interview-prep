from typing import TypeVar

from datastructures.linkedlistnode import SinglyLinkedListNode, DoublyLinkedListNode

T = TypeVar('T')


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0


class SinglyLinkedList(LinkedList):
    """Implements a generic singly linked list.
    Each element has a pointer to the next node in the list. The last elements points to None.
    """

    def __init__(self):
        super().__init__()

    def insert(self, data: T) -> None:
        """Adds an element to the end of the list."""
        new_node = SinglyLinkedListNode(data)
        if not self.head:  # list is empty, head will be new node
            self.head = new_node
            self.size += 1
            return

        # traverse the list from head to tail, add new element to tail
        tail = self.get_tail()
        tail.next = new_node
        self.size += 1

    def remove(self, data: T) -> None:
        """Removes the node and updates pointers. Assumes unique values in data."""
        if self.head and self.head.data == data:
            self.head = None
            return

        prev_node = self.head
        for current_node in self.next_node():
            if not current_node.next:  # reached tail
                prev_node.next = None
                self.size -= 1
                return

            if current_node.data == data:
                prev_node.next = current_node.next
                self.size -= 1
                return
            prev_node = current_node

    def get_tail(self) -> SinglyLinkedListNode:
        """Returns the tail (last element in list) by traversing through it. O(n)."""
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        return current_node

    def next_node(self):
        """Returns the next node. Starts with head."""
        yield self.head
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
            yield current_node

    def size_O_n(self) -> int:
        """Returns the number of nodes. This is the O(n) version of size."""
        if not self.head:
            return 0
        else:
            return sum(1 for node in self.next_node())


class DoublyLinkedList(SinglyLinkedList):
    """Implements a generic doubly linked list.
    Each node has a pointer its previous as well as next node.
    Head is indicated by node.prev = None. Tail is indicated by node.next = None
    """

    def __init__(self):
        super().__init__()

