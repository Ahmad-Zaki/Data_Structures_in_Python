"""
Author: Ahmad Elkholi

Created on Wed Oct 20 13:54:12 2022

Stack data structure implementations using lists and linked lists.

"""
from typing import Any

FULL_STACK_ERROR_MSG = "Maximum stack capacity reached, unable to store more elements."
EMPTY_STACK_ERROR_MSG = "Stack is empty."


class Stack:
    """List-based implementation of Stack data structure.
    
    Parameters
    ----------
    capacity: int
        Determine the maximum amount of elements a Stack can carry. If unspecified, Stack capacity will be limitless.
        default = None

    vals: iterable
        a group of elements that are added to the Stack during its construction. If unspecified, an empty Stack is created. If the number of elements in vals exceeds the specified capacity, An assertion error is raised.
        default = None

    Methods
    -------
    empty() -> bool:
        Check if the stack is empty.

    full() -> bool:
        Check if the stack is full.

    push(element) -> self:
        Add an element to the top of the stack.

    pop() -> Any:
        Remove the top element in the stack.

    peek() -> Any:
        Access the top element of the stack.

    delete() -> None:
        Remove all elements from the stack.
    """

    def __init__(self, capacity: int = None, vals: list = None) -> None:
        self._assert_params(capacity, vals)
        self._capacity = capacity
        self._elements = list(vals) if vals else []
        self._size = len(self._elements)

    def __repr__(self) -> str:
        return f"Stack({self._elements})"

    def __len__(self) -> int:
        return self._size

    def __iter__(self):
        return iter(self._elements)

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
                ), f"Cannot create stack with {len(vals)} elements and max capacity of {capacity}."

    def empty(self) -> bool:
        """Check if the stack is empty."""
        return self._size == 0

    def full(self) -> bool:
        """Check if the stack is full."""
        return self._size == self._capacity

    def push(self, element: Any):
        """Add an element to the top of the stack.
        
        Parameters
        ----------
        element: Any
            The element that is added to the stack.

        Returns
        -------
        self
        """

        assert not self.full(), FULL_STACK_ERROR_MSG

        self._elements.append(element)
        self._size += 1

        return self

    def pop(self) -> Any:
        """Remove the top element in the stack.

        Returns
        -------
        Element: Any
            The top element in the stack.
        """

        assert not self.empty(), EMPTY_STACK_ERROR_MSG

        self._size -= 1
        return self._elements.pop()

    def peek(self) -> Any:
        """Access the top element of the stack.

        Returns
        -------
        Element: Any
            The top element in the stack.
        """

        assert not self.empty(), EMPTY_STACK_ERROR_MSG

        return self._elements[-1]

    def delete(self) -> None:
        """Remove all elements from the stack."""
        self._elements = []
        self._size = 0
