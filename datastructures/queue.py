from typing import TypeVar


class Queue:
    """Implements a queue for a generic data type.
    Queues use the FIFO (first in, first out) principle.
    """

    T = TypeVar('T')

    def __init__(self):
        self.items = []

    def add(self, item: T) -> None:
        """Adds an item to the end of the queue.
        """
        self.items.append(item)

    def remove(self) -> T:
        """Removes the first item of the queue.
        """
        return self.items.pop(0)

    def peek(self) -> T:
        """Shows the first item in the queue
        """
        return self.items[0]

    def size(self) -> int:
        """Returns the current size of the queue.
        """
        return len(self.items)

    def is_empty(self) -> bool:
        """Returns whether the stack is empty or not.
        """
        return len(self.items) == 0
