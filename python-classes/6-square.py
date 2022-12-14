#!/usr/bin/python3
"""class Square defines a square:
- Size : Private instance attribute
- Instantiation with size (no type/value verification)
"""
class Square:
    """
    The class Square define a square
    """
  
    def __init__(self, size=0, position=(0, 0)):
  
        """
        The __init__ method is used. This method run as soon as an object of
        a classe is instantiated (= created).
        Args:
        size (int): the size of the square, must be an integer
        Attribute:
        - __size: the size is a private attribute (that means the acces to
        variable size is restricted)

        Raises:
        TypeError: is not a int
        ValueError: is negative
        """
        self.__size = size
        self.__position = position
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
           raise ValueError("size must be >= 0")

        if type(position) != tuple or len(position) != 2 or \
           type(position[0]) != int or position[0] < 0 or \
	   type(position[1]) != int or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
    
    @property
    def size(self):
        """
        @property method retrieve the data.
        Return the size of a square
        """

        return self.__size

    @size.setter
    def size(self, value):
       
        """
        @size.setter method change the data.
        Args:
        - value (int): the size of the square, must be an integer
        """
        self.__size = value
	
        if type(size) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
         """
         @position.setter method change the square's position
         Args:
         - value (tuple): the position of the square, must be a tuple
         and 2 positive integers
         """

         self.__position = value
        
         if type(value) != tuple or len(value) != 2 or \
           type(value[0]) != int or value[0] < 0 or \
	   type(value[1]) != int or value[1] < 0:
           raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        The area method is a public instance.
        Return the current square area
        """
        return self.__size ** 2



    def my_print(self):
        """
        The my_print method prints in stdout
        the square with '#'
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end="")
                for m in range(self.size):
                    print("#", end="")
                print()
