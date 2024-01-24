#!/usr/bin/python3

"""
Module 100-singly_linked_list
defines a singly linked list with private attribute, head, a public method
that inserts a new Node into the correct sorted position in the list
(increasing order)
"""


class Node:
    """
    defines a node of a singly linked list
    """
    def __init__(self, data, next_node=None):
        """
        Initialize a node  and its next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        get node data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        set data and validate
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        retrieve(get) next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        set next node
        """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    defines a singly linked list class
    """
    def __init__(self):
        """
        Initializes a single linked list
        """
        self.__head = None

    def __str__(self):
        """
        string representation o singly linked list neded for print
        """
        listStr = ""
        current = self.__head
        while current is not None:
            listStr += str(current.data)
            current = current.next_node
            if current is not None:
                listStr += "\n"
        return listStr

    def sorted_insert(self, value):
        """
        inserts a new Node into the correct sorted
        position in the list (increasing order)
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return

        current = self.__head
        if new.data < current.data:
            new.next_node = self.__head
            self.__head = new
            return

        while (current.next_node is not None) and \
              (new.data > current.next_node.data):
            current = current.next_node
        new.next_node = current.next_node
        current.next_node = new
        return
