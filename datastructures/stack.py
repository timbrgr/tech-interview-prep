from typing import TypeVar


class Stack:
    """Implements a stack for a generic data type.
    Stacks use the LIFO (last in, first out) principle.
    """

    T = TypeVar('T')

    def __init__(self):
        self.items = []

    def push(self, item: T) -> None:
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self) -> T:
        """Returns the top element of the stack."""
        return self.items.pop()

    def peek(self) -> T:
        """Shows the top element of the stack."""
        return self.items[-1]

    def size(self) -> int:
        """Returns the current size of the stack."""
        return len(self.items)

    def is_empty(self) -> bool:
        """Returns whether the stack is empty or not."""
        return len(self.items) == 0
