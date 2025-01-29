#!/usr/bin/python3
"""
    Task 5: Square Class
"""


class Square:
    """Defines a square """
    def __init__(self, size=0):
        """Initializes the Square instance with a given size (default is 0)"""
        self.size = size

    def area(self):
        """Calculates and returns the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """Getter method for the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        performs type and value validation
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints a square made of hash symbols (#)"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
