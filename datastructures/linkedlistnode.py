from typing import TypeVar, Generic

T = TypeVar('T')


class LinkedListNode(Generic[T]):

    """Implementation of a generic linked list node.
    Each node only holds data.
    """

    def __init__(self, data: T):
        self.data = data


class SinglyLinkedListNode(LinkedListNode):
    """Implementation of a generic singly linked list node.
    Each node has a pointer to its next node.
    """

    def __init__(self, data: T):
        super().__init__(data)
        self.next = None


class DoublyLinkedListNode(SinglyLinkedListNode):
    """Implementation of a generic doubly linked list node.
    Each node has a pointer to its previous as well as next node.
    """

    def __init__(self, data: T, prev: LinkedListNode):
        super().__init__(data)
        self.prev = prev
