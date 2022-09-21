#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
   
    
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        self.__size = value
        if type(size) != int:
            raise TypeError("size must be an integer")
        if  size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
   
    @property
    def position(self):
        return self.__position 
   
    @position.setter
    def position(self, value):
        self.__position = value
       
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
    
    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
      	   print("")
        elif self.position[1] > 0:
            for pos1 in range(self.__position[1]):
                print("")

        for line in range(self.__size):
            for pos0 in range(self.__position[0]):
                print(" ", end="")
        for column in range(self.__size):
            print("#", end="")
        print("")
