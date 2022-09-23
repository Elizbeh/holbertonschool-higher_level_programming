#!/usr/bin/python3
"""
A function to adding two integersi
"""


def add_integer(a, b=98):
    
    """Take the arguments to add.
    
    a: One of the numbers, default not defined.
    b: The other number, set to default 98.

    Return:
        int(a) + int (b)
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
