#!/usr/bin/env python3


class Node:
    """
    A class representing a node in a linked list.

    Attributes:
        data: The data stored in the node.
        next: Reference to the next node in the linked list.
    """

    def __init__(self, data=None):
        """
        Initializes a new node.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.next = None


class SLL:
    """
    A class representing a singly linked list.

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
        print('Linked List: ')
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
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = self.head

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
            self.tail = new_node

    def add_after(self, node, new_data):
        """
        Adds a node after the given node.

        Args:
             node: The node after which the new node is to be added.
             new_data: The data for the new node.
        """
        new_node = Node(new_data)
        new_node.next = node.next
        node.next = new_node
        if self.tail == node:
            self.tail = new_node

    def pop_front(self):
        """
        Removes a node from the beginning of the linked list.
        """
        if self.head is None:
            print('Error: Empty list.')
            return
        self.head = self.head.next
        if self.head is None:
            self.tail = None

    def pop_back(self):
        """
        Removes a node from the end of the linked list.
        """
        if self.head is None:
            print('Error: Empty list.')
            return
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            pointer = self.head
            while pointer.next.next is not None:
                pointer = pointer.next
            self.tail = pointer
            self.tail.next = None


if __name__ == "__main__":
    l1 = SLL()
    l1.pop_front()
