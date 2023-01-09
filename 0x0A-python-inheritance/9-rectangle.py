#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height) -> None:
        self.__width = width
        self.__height = height
        

        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __repr__(self) -> str:
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        return self.__width * self.__height
