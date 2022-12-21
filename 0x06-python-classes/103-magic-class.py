#!/usr/bin/python3

import math

"""Class Magic"""


class MagicClass:
    def __init__(self, radius):
        """
        Class initializer
        """

        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        area calc func
        """

        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        circumference calc func
        """

        return 2 * math.pi * self.__radius
