from abc import ABC, abstractmethod

from datastructures.types import CT


class Heap(ABC):
    """Implements a generic heap with comparable type."""

    def __init__(self):
        self.size = 0
        self.items = []

    @staticmethod
    def get_left_child_idx(idx_parent: int) -> int:
        return int(idx_parent * 2 + 1)

    @staticmethod
    def get_right_child_idx(idx_parent: int) -> int:
        return int(idx_parent * 2 + 1)

    @staticmethod
    def get_parent_idx(child_idx: int) -> int:
        return int((child_idx - 2) / 2)

    def has_left_child(self, idx: int) -> bool:
        return self.get_left_child_idx(idx) < self.size

    def has_right_child(self, idx: int) -> bool:
        return self.get_right_child_idx(idx) < self.size

    def has_parent(self, idx: int) -> bool:
        return self.get_parent_idx(idx) >= 0

    def left_child(self, idx: int) -> CT:
        return self.items[self.get_left_child_idx(idx)]

    def right_child(self, idx: int) -> bool:
        return self.items[self.get_right_child_idx(idx)]

    def parent(self, idx: int) -> bool:
        return self.items[self.get_parent_idx(idx)]

    def swap(self, idx_one: int, idx_two: int) -> None:
        temp = self.items[idx_one]
        self.items[idx_one] = self.items[idx_two]
        self.items[idx_two] = temp

    def peek(self) -> CT:
        if not self.items:
            raise ValueError()
        return self.items[0]

    def poll(self) -> CT:
        """Removes and returns min element."""
        item = self.items[0]
        self.items[0] = self.items[-1]  # swap last element with root
        self.heapify_down()
        self.size -= 1
        return item

    def add(self, item: CT) -> None:
        self.items.append(item)
        self.size += 1
        self.heapify_up()

    @abstractmethod
    def get_comparator(self, idx_one: int, idx_two: int): ...

    def heapify_down(self):
        idx = 0  # start at root
        while self.has_left_child(idx):  # if has_right_child, must have a left child
            child_idx = self.get_most_interesting_child_idx(idx)

            if self.get_comparator(idx, child_idx):
                break
            self.swap(idx, child_idx)
            idx = child_idx

    def get_most_interesting_child_idx(self, idx: int) -> int:
        """Returns the "most interesting child" depending on heap implementation.
        MinHeap: child with smaller value.
        MaxHeap: child with bigger value.
        """
        interesting_child_idx = self.left_child(idx)
        if self.has_right_child(idx) and \
                not self.get_comparator(self.get_left_child_idx(idx),
                                        self.get_right_child_idx(idx)):
            interesting_child_idx = self.get_right_child_idx(idx)
        return interesting_child_idx

    def heapify_up(self):
        idx = self.size - 1  # "bubble up" last element added
        while self.has_parent(idx) and self.get_comparator(idx, self.get_parent_idx(idx)):
            self.swap(idx, self.get_parent_idx(idx))
            idx = self.get_parent_idx(idx)


class MinHeap(Heap):
    """Implements min heap for a comparable type."""

    def __init__(self):
        super().__init__()

    def get_comparator(self, idx_one: int, idx_two: int):
        """Returns True if child is less than parent's value."""
        return self.items[idx_one] < self.items[idx_two]


class MaxHeap(Heap):
    """Implements max heap for a comparable type."""

    def __init__(self):
        super().__init__()
        raise NotImplementedError()

    def get_comparator(self, idx_one: int, idx_parent):
        """Returns True if child is greater than parent's value."""
        return self.items[idx_one] > self.parent(idx_one)
