#!/usr/bin/python3
"""The function that prints My name is <first name> <last name>"""


def test_say_my_name(first_name, last_name=""):
    """function that print the full name

    Arguments:
        first_name (str): the frist name
        last_name (str, optional): the last name. Defaults to "".
    """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    elif isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
