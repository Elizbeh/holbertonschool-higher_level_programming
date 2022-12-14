#!/usr/bin/python3
"""Class Square defines a square:
- Size : Private instance attribute
- Instantiation with size (no type/value verification)
"""


class Square:
    """
    The class Square define a square
    """
    
    def __init__(self, size=0):

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
     
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
    
    def area(self):
        """
        The area method is a public instance.
	Return the current square area
	"""
        return self.__size ** 2
    
