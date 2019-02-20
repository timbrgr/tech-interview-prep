from typing import TypeVar


class LinkedListNode:
    """Implementation of a generic linked list node.
    """

    T = TypeVar('T')

    def __init__(self, data: T):
        self.data = data
        self.next = None
