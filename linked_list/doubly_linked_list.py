#!/usr/bin/env python3


class Node:
    """
    A class representing a node in a linked list.
    
    Attributes:
        data: The data stored in the node.
        next: Reference to the next node in the linked list.
        prev: Reference to the previous node in the linked list.
    """

    def __init__(self, data=None):
        """
        Initializes a new node.
    
        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    """
    A class representing a doubly linked list.
    
    Attributes:
        head: Reference to the first node in the linked list.
        tail: Reference to the last node in the linked list.
    """

    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.head = self.tail = None

    def print_list(self):
        """
        Prints the elements of the linked list.
        """
        pointer = self.head
        print('Linked list: ')
        while pointer is not None:
            print(pointer.data)
            pointer = pointer.next

    def push_front(self, new_data):
        """
        Adds a new node at the beginning of the linked list.
        
        Args:
            new_data: The data for the new node.
        """
        new_node = Node(new_data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def push_back(self, new_data):
        """
        Adds a new node at the end of the linked list.
        
        Args:
            new_data: The data for the new node.
        """
        new_node = Node(new_data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node


if __name__ == '__main__':
    l1 = DLL()
    l1.head = l1.tail = Node('1')
    l1.print_list()
