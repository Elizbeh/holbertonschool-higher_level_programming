#!/usr/bin/python3
"""
The BaseGeometry class
"""


class BaseGeometry:
    """
    The class BaseGeometry
    """
    def area(self):
        """
        Instance method that raises an Exception with the message
        "area() is not implemented."
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Instance method that validates value
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
