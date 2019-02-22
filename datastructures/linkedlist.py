from typing import TypeVar, Iterable

from datastructures.linkedlistnode import SinglyLinkedListNode, DoublyLinkedListNode

T = TypeVar('T')


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
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
            self.tail = self.head
            self.size += 1
            return

        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def remove(self, data: T) -> None:
        """Removes the node and updates pointers. Assumes unique values in data."""
        if self.head and self.head.data == data:
            self.head = self.head.next
            return

        prev_node = self.head
        for current_node in self.next_node_start_from_head():
            if not current_node.next and current_node.data == data:  # reached tail
                self.tail = prev_node
                prev_node.next = None
                self.size -= 1
                return

            if current_node.data == data:
                prev_node.next = current_node.next
                self.size -= 1
                return
            prev_node = current_node

    def get_tail_O_n(self) -> SinglyLinkedListNode:
        """Returns the tail (last element in list) by traversing through it. O(n)."""
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        return current_node

    def next_node_start_from_head(self) -> Iterable[SinglyLinkedListNode]:
        """Returns the next node. Starts with head. Traverses the list forward."""
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
            return sum(1 for node in self.next_node_start_from_head())


class DoublyLinkedList(SinglyLinkedList):
    """Implements a generic doubly linked list.
    Each node has a pointer its previous as well as next node.
    Head is indicated by node.prev = None. Tail is indicated by node.next = None
    """

    def __init__(self):
        super().__init__()

    def insert(self, data: T) -> None:
        """Adds an element to the end of the list."""
        if not self.head:
            new_node = DoublyLinkedListNode(data, prev=None)
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return

        new_node = DoublyLinkedListNode(data, prev=self.tail)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def remove(self, data: T) -> None:
        """Removes the node and updates pointers. Assumes unique values in data."""
        if self.head and self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return

        for current_node in self.next_node_start_from_head():
            if not current_node.next and current_node.data == data:  # reached tail
                self.tail = current_node.prev
                current_node.prev = None
                self.size -= 1
                return

            if current_node.data == data:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
                self.size -= 1
                return

    def previous_node_start_from_tail(self) -> Iterable[DoublyLinkedListNode]:
        """Returns the previous node. Starts with tail. Traverses the list backward."""
        yield self.tail
        current_node = self.tail
        while current_node.prev:
            current_node = current_node.prev
            yield current_node
