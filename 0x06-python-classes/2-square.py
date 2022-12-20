#!/usr/bin/python3

class Square:
    """
    Simple class Square
    """

    def __init__(self, size=0):
        self.__size = size
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            elif type(size) != int:
                raise TypeError("size must be an integer")
        except (ValueError, TypeError) as e:
            print(e)
        except Exception:
            pass
