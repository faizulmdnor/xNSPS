# data_types.py

"""
Module: data_types
Description: A module to demonstrate and provide utility functions for common Python data types.
Author: Faizul Md Nor
"""


# Function to demonstrate and explain data types

def explain_data_types():
    """
    :return: This function prints out descriptions of various basic data types in Python such as integers, floats, strings, lists, tuples, sets, and dictionaries.
    """
    print("1. Integers: Whole numbers, e.g., 10, -5")
    print("2. Floats: Decimal numbers, e.g., 3.14, -2.5")
    print("3. Strings: Text data, e.g., 'Hello', 'Python'")
    print("4. Lists: Ordered, mutable collections, e.g., [1, 2, 3], ['apple', 'banana']")
    print("5. Tuples: Ordered, immutable collections, e.g., (1, 2, 3), ('a', 'b')")
    print("6. Sets: Unordered collections with unique elements, e.g., {1, 2, 3}, {'apple', 'banana'}")
    print("7. Dictionaries: Key-value pairs, e.g., {'name': 'Faizul', 'age': 35}")


# Utility functions for each data type

def add_integers(a, b):
    """
    :param a: The first integer to be added.
    :param b: The second integer to be added.
    :return: The sum of the two integers.
    :raises ValueError: If either of the arguments is not an integer.
    """
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        raise ValueError("Both arguments must be integers.")


def multiply_floats(a, b):
    """
    :param a: First number to multiply. Must be a float.
    :param b: Second number to multiply. Must be a float.
    :return: The product of a and b.
    :raises ValueError: If either a or b is not a float.
    """
    if isinstance(a, float) and isinstance(b, float):
        return a * b
    else:
        raise ValueError("Both arguments must be floats.")


def concat_strings(s1, s2):
    """
    :param s1: The first string to be concatenated.
    :param s2: The second string to be concatenated.
    :return: The concatenated result of s1 and s2.
    :raises ValueError: If either s1 or s2 is not a string.
    """
    if isinstance(s1, str) and isinstance(s2, str):
        return s1 + s2
    else:
        raise ValueError("Both arguments must be strings.")


def list_append(lst, element):
    """
    :param lst: The list to which the element will be appended.
    :type lst: list
    :param element: The element to append to the list.
    :return: The list with the element appended.
    :rtype: list
    :raises ValueError: If the first argument is not a list.
    """
    if isinstance(lst, list):
        lst.append(element)
        return lst
    else:
        raise ValueError("First argument must be a list.")


def tuple_access(tup, index):
    """
    :param tup: The tuple from which to retrieve an element.
    :type tup: tuple
    :param index: The index of the element to retrieve from the tuple.
    :type index: int
    :return: The element at the given index in the tuple.
    :rtype: Any
    :raises IndexError: If the provided index is out of the tuple's range.
    :raises ValueError: If the first argument is not a tuple or the second argument is not an integer.
    """
    if isinstance(tup, tuple) and isinstance(index, int):
        try:
            return tup[index]
        except IndexError:
            raise IndexError("Index out of range for the tuple.")
    else:
        raise ValueError("First argument must be a tuple, second an integer index.")


def set_add(s, element):
    """
    :param s: The set to which the element is to be added. Must be a set object.
    :param element: The element to add to the set.
    :return: The set with the new element added if the input is valid.
    :raises ValueError: If the first argument is not a set.
    """
    if isinstance(s, set):
        s.add(element)
        return s
    else:
        raise ValueError("First argument must be a set.")


def dict_get(d, key):
    """
    :param d: Dictionary to search for the key.
    :param key: Key to search for in the dictionary.
    :return: Value associated with the key if found, else "Key not found".
    :raises ValueError: If the first argument is not a dictionary.
    """
    if isinstance(d, dict):
        return d.get(key, "Key not found")
    else:
        raise ValueError("First argument must be a dictionary.")


# Test functionality
if __name__ == "__main__":
    explain_data_types()

    # Test functions
    print(add_integers(5, 10))  # 15
    print(multiply_floats(2.5, 4.0))  # 10.0
    print(concat_strings("Hello, ", "world!"))  # "Hello, world!"
    print(list_append([1, 2, 3], 4))  # [1, 2, 3, 4]
    print(tuple_access((10, 20, 30), 1))  # 20
    print(set_add({1, 2, 3}, 4))  # {1, 2, 3, 4}
    print(dict_get({"name": "Faizul", "age": 35}, "name"))  # "Faizul"
