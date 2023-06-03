# This script demonstrates common Python errors.

# ZeroDivisionError
def zero_division():
    """This function demonstrates a ZeroDivisionError."""
    return 1 / 0

print("ZeroDivisionError example:")
try:
    zero_division()
except ZeroDivisionError:
    print("Caught a ZeroDivisionError: Cannot divide by zero\n")


# ValueError
def value_error():
    """This function demonstrates a ValueError."""
    return int("abc")

print("ValueError example:")
try:
    value_error()
except ValueError:
    print("Caught a ValueError: Cannot convert string to integer\n")


# IndexError
def index_error():
    """This function demonstrates an IndexError."""
    list = [1, 2, 3]
    return list[5]

print("IndexError example:")
try:
    index_error()
except IndexError:
    print("Caught an IndexError: Index out of range\n")


# KeyError
def key_error():
    """This function demonstrates a KeyError."""
    dict = {'a': 1, 'b': 2, 'c': 3}
    return dict['d']

print("KeyError example:")
try:
    key_error()
except KeyError:
    print("Caught a KeyError: Key not found in dictionary\n")


# NameError
def name_error():
    """This function demonstrates a NameError."""
    return undefined_variable

print("NameError example:")
try:
    name_error()
except NameError:
    print("Caught a NameError: Variable not defined\n")


# TypeError
def type_error():
    """This function demonstrates a TypeError."""
    return "abc" + 1

print("TypeError example:")
try:
    type_error()
except TypeError:
    print("Caught a TypeError: Cannot add string and integer\n")
