# Lambda Functions in Python

# Lambda function with one argument
square = lambda x: x ** 2
print(f"The square of 5 is {square(5)}")  # Output: 25

# Lambda function with multiple arguments
multiply = lambda x, y: x * y
print(f"The product of 3 and 4 is {multiply(3, 4)}")  # Output: 12

# Lambda function used in a list comprehension
numbers = [1, 2, 3, 4, 5]
squared = [(lambda x: x ** 2)(x) for x in numbers]
print(f"The squares of the numbers {numbers} are {squared}")  # Output: [1, 4, 9, 16, 25]

# Lambda function used with built-in functions

# Using map()
squared = list(map(lambda x: x ** 2, numbers))
print(f"The squares of the numbers {numbers} are {squared}")  # Output: [1, 4, 9, 16, 25]

# Using filter()
even = list(filter(lambda x: x % 2 == 0, numbers))
print(f"The even numbers in the list {numbers} are {even}")  # Output: [2, 4]

# Using reduce()
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(f"The product of the numbers {numbers} is {product}")  # Output: 120
