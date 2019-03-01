from abc import ABC, abstractmethod
from typing import Any, TypeVar


class Comparable(ABC):
    @abstractmethod
    def __lt__(self, other: Any) -> bool: pass

    @abstractmethod
    def __le__(self, other: Any) -> bool: pass

    @abstractmethod
    def __eq__(self, other: Any) -> bool: pass

    @abstractmethod
    def __ge__(self, other: Any) -> bool: pass

    @abstractmethod
    def __gt__(self, other: Any) -> bool: pass


CT = TypeVar('CT', bound=Comparable)
