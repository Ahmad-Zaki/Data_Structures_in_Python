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
        self.__assert_params(capacity, vals)
        self.__capacity = capacity
        self.__elements = list(vals) if vals else []
        self.__size = len(self.__elements)

    def __repr__(self) -> str:
        return f"Queue({self.__elements})"

    def __len__(self) -> int:
        return self.__size

    def __iter__(self):
        self.__queue_iterator = iter(self.__elements)
        return self

    def __next__(self) -> Any:
        return next(self.__queue_iterator)

    def __contains__(self, element) -> bool:
        return element in self.__elements

    def __assert_params(self, capacity, vals) -> None:
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
        return self.__size == 0

    def full(self) -> bool:
        """Check if the queue is full."""
        return self.__size == self.__capacity

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

        self.__elements.append(element)
        self.__size += 1

        return self

    def dequeue(self) -> Any:
        """pop the first element in the queue.

        Returns
        -------
        Element: Any
            The first element in the queue.
        """

        assert not self.empty(), EMPTY_QUEUE_ERROR_MSG

        self.__size -= 1
        return self.__elements.pop(0)

    def peek(self) -> Any:
        """Access the first element of the queue.

        Returns
        -------
        Element: Any
            The first element in the queue.
        """

        assert not self.empty(), EMPTY_QUEUE_ERROR_MSG

        return self.__elements[0]

    def delete(self) -> None:
        """Remove all elements from the Queue."""
        self.__elements = []
        self.__size = 0


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
        self.__assert_params(capacity, vals)
        self.__capacity = capacity
        self.__elements = SinglyLL(vals)
        self.__size = len(self.__elements)

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

        self.__elements.insert(element)
        self.__size += 1

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
        self.__elements.pop(0)
        self.__size -= 1
        return removed_element

    def delete(self) -> None:
        """Remove all elements from the Queue."""
        self.__elements.delete()
        self.__size = 0


class QueueCirc:
    def __init__(self, capacity: int) -> None:
        self.__capacity = capacity
        self.__elements = capacity * [None]
        self.__first = -1
        self.__last = -1
        self.__size = 0

    def __len__(self) -> int:
        return self.__size

    def empty(self) -> bool:
        """Check if the queue is empty."""
        return self.__size == 0

    def full(self) -> bool:
        """Check if the queue is full."""
        return self.__size == self.__capacity

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

        if self.empty():
            self.__first = self.__last = 0
        else:
            self.__last = (self.__last + 1) % self.__capacity

        self.__elements[self.__last] = element
        self.__size += 1
        return self

    def dequeue(self) -> Any:
        """pop the first element in the queue.

        Returns
        -------
        Element: Any
            The first element in the queue.
        """

        assert not self.empty(), EMPTY_QUEUE_ERROR_MSG

        removed_element = self.__elements[self.__first]
        self.__elements[self.__first] = None

        self.__size -= 1
        if self.__size == 0:
            self.__first = self.__last = -1
        else:
            self.__first = (self.__first + 1) % self.__capacity

        return removed_element

    def peek(self) -> Any:
        """Access the first element in the queue.

        Returns
        -------
        Element: Any
            The first element in the queue.
        """

        assert not self.empty(), EMPTY_QUEUE_ERROR_MSG

        return self.__elements[self.__first]

    def delete(self) -> None:
        """Remove all elements from the Queue."""
        self.__elements = self.__capacity * [None]
        self.__first = self.__last = -1
        self.__size = 0
