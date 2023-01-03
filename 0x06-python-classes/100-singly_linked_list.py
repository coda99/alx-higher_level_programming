#!/uar/bin/python3

""" Class Node """


class Node:
    """
    This is Node representation
    """

    def __init__(self, data, next_node=None):
        """
        Class initializer
        """

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        getter method for data
        """

        return self.__data

    @data.setter
    def data(self, value):
        """
        setter method for data
        """

        self.__data = value

    @property
    def next_node(self):
        """
        getter method for next_node
        """

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        setter method for next_node
        """

        self.__next_node = value


class SinglyLinkedList:
    """
    class SinglyLinkedList
    """

    def __init__(self):
        """
        class initializer
        """

        self.__head = None

    def sorted_insert(self, value):




