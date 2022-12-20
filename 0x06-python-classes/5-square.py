#!/usr/bin/python3

class Square:
    """
    Simple class Square
    """

    def __init__(self, size=None):
        self.__size = size

        try:
            if self.__size < 0:
                raise ValueError("size must be >= 0")

        except ValueError as e:
            print(e)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        try:
            if type(self.__size) == str:
                raise TypeError("size must be integer")
            elif self.__size <= 0:
                print()
            for i in range(self.__size):
                print("#" * self.__size)
        except TypeError as e:
            print(e)
