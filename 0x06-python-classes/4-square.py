#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """class square that has attributes size"""
    def __init__(self, size=0):
        """initialization function for our square clasee"""
        self.size = size

    @property
    def size(self):
        """it will Get/set the current size of the square."""
        return self.

    @size.setter
    def size(self, value):
        """set the size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
