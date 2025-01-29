#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """ Define a class Square."""

    def __init__(self, size=0, position=(0, 0)):
        """initialize method"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """property method"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter method"""
        if (type(value) is not int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """position method"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter method"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(not isinstance(i, int)
               for i in value) or any(j < 0 for j in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):

        return (self.__size * self.__size)

    def my_print(self):
        """prints square with the char #"""
        if self.size == 0:
            print()
        else:
            i, j = self.position
            for line in range(j):
                print()
            for line in range(self.size):
                print(' ' * i, end='')
                print('#' * self.size)
