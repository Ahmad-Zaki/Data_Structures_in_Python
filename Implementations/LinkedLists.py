"""
Author: Ahmad Elkholi

Created on Fri Feb 25 16:58:57 2022

"""
from abc import ABC, abstractmethod

class Node:
    '''Create a singly linked list node'''
    def __init__(self, data = None):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f"Node({self.data})"

class LinkedList(ABC):
    '''Base Class for linked lists implementations'''
    def __init__(self, vals: list = None, *, circular: bool = False) -> None:
        self.head = None
        self.tail = None
        self.circular = circular
        self._length = 0
        if vals:
            for val in vals:
                self.insert(val)

    def __len__(self) -> int:
        return self._length

    def __iter__(self):
        self.__node = self.head
        return self

    def __next__(self) -> Node:
        if self.__node is None: 
            raise StopIteration
        node = self.__node
        if self.circular and self.__node == self.tail:
            self.__node = None
        else:
            self.__node = self.__node.next
        return node

    def __getitem__(self, index: int) -> Node:
        if index < 0: 
            index = max(0, self._length + index)
        self._validate_index(index)

        node = self.head
        for _ in range(index):
            node = node.next
        return node

    def __contains__(self, val) -> bool:
        for node in self:
            if node.data == val: return True
        return False

    def _validate_index(self, index: int) -> None:
        """Validate index value."""
        assert self._length > 0, "List is empty"

        if not isinstance(index, int):
            raise TypeError(f"Invalid type {type(index)}. Index must be int")
        
        if index not in range(self._length):
            raise IndexError(f"Index out of bound, please specify an index between 0 and {self._length-1}") 

    @abstractmethod
    def insert(self, val):
        pass

    def delete(self) -> None:
        '''Delete all elements of a linked list.
        
        Once you set the head & tail to None, the garpage collector will delete all nodes one by one.
        '''

        self.head = None
        self.tail = None
        self._length = 0

class SinglyLL(LinkedList):
    """Single Linked List Class

    Parameters
    ----------
    vals: list, tuple
        values of the nodes in the linked list. Values are added in their same order in vals.
        default = None

    circular: bool
        Whether the list is circular or not. Must be specified as a keyword argument if you want to set it to True.
        default = False
    
    Methods
    -------
    insert(val, index: int = None)
        Insert a node containing the given value in the specified index.

    def pop(index: int = None)
        Remove the node with the specified index from the Linked List.

    def remove(val):
        Remove the node with the specified value from the Linked List.

    delete():
        Delete all elements of a linked list.
    """

    def __repr__(self) -> str:
        values = []
        for node in self:
            values.append(str(node.data))
        return "->".join(values)

    def insert(self, val, index: int = None):
        """Insert a node containing the given value to the linked list in the specified index.
        
        Parameters
        ----------
        val:
            The value contained in the added node
            
        index: int
            The index of the added node in the linked list. if unspecified, the node will be added at the end of the list
            default = None
            
        Returns
        -------
        self
        """

        if index == None: index = self._length

        if not isinstance(index, int):
            raise TypeError(f"Invalid type {type(index)}. Index must be int")
        
        if index not in range(self._length + 1):
            raise IndexError(f"index out of bound, please specify an index between 0 and {self._length}") 

        new_node = Node(val)

        if self.head is None:
            #If list has no nodes, assign node as both head and tail.
            self.head = new_node
            self.tail = new_node

        elif index == 0:
            #The new node is added to the beginning of the list.
            new_node.next = self.head
            self.head = new_node

        elif index == self._length:
            #The new node is added to the end of the list.      
            self.tail.next = new_node
            self.tail = new_node 
        else:
            #The new node is added to the middle of the list.
            previous_node = self.head
            for _ in range(index-1):
                previous_node = previous_node.next
            new_node.next = previous_node.next
            previous_node.next = new_node

        if self.circular: self.tail.next = self.head
        self._length += 1
        return self

    def pop(self, index: int = None):
        """Remove the node with the specified index from the Linked List.
        
        Parameters
        ----------
        index: int
            The index of the deleted node in the linked list. if unspecified, the last node will be removed.
            default = None
            
        Returns
        -------
        self
        """

        #If the list is already empty, return.
        if self.head is None: 
            return self

        if index == None: 
            index = self._length - 1

        if not isinstance(index, int):
            raise TypeError(f"Invalid type {type(index)}. Index must be int")
        
        if index not in range(self._length):
            raise IndexError(f"index out of bound, please specify an index between 0 and {self._length}") 

        if index == 0:
            if self.head == self.tail:
                #If the linked list has only one node.
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                if self.circular: self.tail.next = self.head
        else:
            previous_node = self.head
            #Find the node that is directly before the deleted node.
            for _ in range(index-1):
                previous_node = previous_node.next

            previous_node.next = previous_node.next.next
            #If the deleted node is the last node then assign previous_node to the tail.
            if previous_node.next is None or previous_node.next == self.head:
                 self.tail = previous_node

        self._length -= 1
        return self

    def remove(self, val):
        """Remove the node with the specified value from the Linked List.
        
        Parameters
        ----------
        val: int
            The val of the deleted node in the linked list.
            
        Returns
        -------
        self
        """

        #If the list is already empty, return.
        if self.head is None: 
            return self

        if self.head.data == val:
            if self.head == self.tail:
                #If the linked list has only one node.
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                if self.circular: self.tail.next = self.head
        else:
            previous_node = self.head
            #Find the node that is directly before the deleted node.
            for node in self:
                if node.data == val: 
                    previous_node.next = node.next
                    break
                previous_node = node
            else:
                raise ValueError(f"'{val}' does not exists in the list.")

            #If the deleted node is the last node then assign previous_node to the tail.
            if previous_node.next is None or previous_node.next == self.head:
                self.tail = previous_node

        self._length -= 1
        return self