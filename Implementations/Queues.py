"""
Author: Ahmad Elkholi

Created on Wed Mar 02 23:54:12 2022

Queue data structure implementations using lists and linked lists, and Circular Queue implementation.

"""
from typing import Any

from LinkedLists import SinglyLL

FULL_QUEUE_ERROR_MSG = "Maximum queue capacity reached, unable to store more elements."
EMPTY_QUEUE_ERROR_MSG = "Queue is empty."


class Queue:
    """List-based implementation of Queue data structure.
    
    Parameters
    ----------
    capacity: int
        Determine the maximum amount of elements a Queue can carry. If unspecified, Queue capacity will be limitless.
        default = None

    vals: iterable
        a group of elements that are added to the Queue during its construction. If unspecified, an empty Queue is created. If the number of elements in vals exceeds the specified capacity, An assertion error is raised.
        default = None

    Methods
    -------
    empty() -> bool:
        Check if the queue is empty.

    full() -> bool:
        Check if the queue is full.

    enqueue(element) -> self:
        Add an element to the end of the queue.

    dequeue() -> Any:
        pop the first element in the queue.

    peek() -> Any:
        Access the first element of the queue.

    delete() -> None:
        Remove all elements from the Queue.
    """

    def __init__(self, capacity: int = None, vals: list = None) -> None:
        self._assert_params(capacity, vals)
        self._capacity = capacity
        self._elements = list(vals) if vals else []
        self._size = len(self._elements)

    def __repr__(self) -> str:
        return f"Queue({self._elements})"

    def __len__(self) -> int:
        return self._size

    def __iter__(self):
        self._queue_iterator = iter(self._elements)
        return self

    def __next__(self) -> Any:
        return next(self._queue_iterator)

    def __contains__(self, element) -> bool:
        return element in self._elements

    def _assert_params(self, capacity, vals) -> None:
        if capacity is not None:
            if not isinstance(capacity, int):
                raise TypeError("capacity must be of type 'int'.")
            if capacity <= 0:
                raise ValueError("capacity must be greater than zero.")

        if vals is not None:
            if not hasattr(vals, "__iter__"):
                raise TypeError("vals is not iterable")
            if capacity is not None:
                assert (
                    len(vals) <= capacity
                ), f"Cannot create queue with {len(vals)} elements and max capacity of {capacity}."

    def empty(self) -> bool:
        """Check if the queue is empty."""
        return self._size == 0

    def full(self) -> bool:
        """Check if the queue is full."""
        return self._size == self._capacity

    def enqueue(self, element: Any):
        """Add an element to the end of the queue.
        
        Parameters
        ----------
        element: Any
            The element that is added to the queue.

        Returns
        -------
        self
        """

        assert not self.full(), FULL_QUEUE_ERROR_MSG

        self._elements.append(element)
        self._size += 1

        return self

    def dequeue(self) -> Any:
        """pop the first element in the queue.

        Returns
        -------
        Element: Any
            The first element in the queue.
        """

        assert not self.empty(), EMPTY_QUEUE_ERROR_MSG

        self._size -= 1
        return self._elements.pop(0)

    def peek(self) -> Any:
        """Access the first element of the queue.

        Returns
        -------
        Element: Any
            The first element in the queue.
        """

        assert not self.empty(), EMPTY_QUEUE_ERROR_MSG

        return self._elements[0]

    def delete(self) -> None:
        """Remove all elements from the Queue."""
        self._elements = []
        self._size = 0


class QueueLL(Queue):
    """LinkedList-based implementation of Queue data structure.
    
    Parameters
    ----------
    capacity: int
        Determine the maximum amount of elements a Queue can carry. If unspecified, Queue capacity will be limitless.
        default = None

    vals: iterable
        a group of elements that are added to the Queue during its construction. If unspecified, an empty Queue is created. If the number of elements in vals exceeds the specified capacity, An assertion error is raised.
        default = None

    Methods
    -------
    empty() -> bool:
        Check if the queue is empty.

    full() -> bool:
        Check if the queue is full.

    enqueue(element) -> self:
        Add an element to the end of the queue.

    dequeue() -> Any:
        pop the first element in the queue.

    peek() -> Any:
        Access the first element of the queue.

    delete() -> None:
        Remove all elements from the Queue.
    """

    def __init__(self, capacity: int = None, vals: list = None) -> None:
        self._assert_params(capacity, vals)
        self._capacity = capacity
        self._elements = SinglyLL(vals)
        self._size = len(self._elements)

    def enqueue(self, element: Any):
        """Add an element to the end of the queue.
        
        Parameters
        ----------
        element: Any
            The element that is added to the queue.

        Returns
        -------
        self
        """

        assert not self.full(), FULL_QUEUE_ERROR_MSG

        self._elements.insert(element)
        self._size += 1

        return self

    def dequeue(self) -> Any:
        """pop the first element in the queue.

        Returns
        -------
        Element: Any
            The first element in the queue.
        """

        assert not self.empty(), EMPTY_QUEUE_ERROR_MSG

        removed_element = self.peek()
        self._elements.pop(0)
        self._size -= 1
        return removed_element

    def delete(self) -> None:
        """Remove all elements from the Queue."""
        self._elements.delete()
        self._size = 0


class QueueCirc(Queue):
    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._elements = capacity * [None]
        self._first = 0
        self._last = -1
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def empty(self) -> bool:
        """Check if the queue is empty."""
        return self._size == 0

    def full(self) -> bool:
        """Check if the queue is full."""
        return self._size == self._capacity

    def enqueue(self, element: Any):
        """Add an element to the end of the queue.
        
        Parameters
        ----------
        element: Any
            The element that is added to the queue.

        Returns
        -------
        self
        """

        assert not self.full(), FULL_QUEUE_ERROR_MSG

        self._last = (self._last + 1) % self._capacity
        self._elements[self._last] = element
        self._size += 1
        return self

    def dequeue(self) -> Any:
        """pop the first element in the queue.

        Returns
        -------
        Element: Any
            The first element in the queue.
        """

        assert not self.empty(), EMPTY_QUEUE_ERROR_MSG

        removed_element = self._elements[self._first]
        self._elements[self._first] = None
        self._first = (self._first + 1) % self._capacity
        self._size -= 1
        return removed_element

    def peek(self) -> Any:
        """Access the first element in the queue.

        Returns
        -------
        Element: Any
            The first element in the queue.
        """

        assert not self.empty(), EMPTY_QUEUE_ERROR_MSG

        return self._elements[self._first]

    def delete(self) -> None:
        """Remove all elements from the Queue."""
        self._elements = self._capacity * [None]
        self._first = 0
        self._last = -1
        self._size = 0
