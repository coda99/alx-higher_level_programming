#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    def __init__(self, size) -> None:
        self.__size = size

        self.integer_validator("size", size)
    
    def __repr__(self) -> str:
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        return self.__size * self.__size
