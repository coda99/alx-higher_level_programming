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

            elif type(size) != int:
               raise TypeError("size must be an integer")

        except (ValueError, TypeError) as e:
            print(e)

    def area(self):
        return self.__size ** 2
