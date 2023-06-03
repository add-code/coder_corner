# Python Functions Tutorial

def add_numbers(num1, num2):
    """This function adds two numbers and returns the result."""
    return num1 + num2

# Call the function and print the result
result = add_numbers(3, 5)
print(f"The sum of 3 and 5 is {result}")

def greet(name, message="Hello"):
    """This function greets a person with a given message. 
    If no message is provided, it defaults to "Hello"
    """
    print(f"{message}, {name}")

# Call the function with and without a message
greet("Alice")  
greet("Bob", "Good morning")

def greet_all(*names):
    """This function greets all the persons in the names tuple."""
    for name in names:
        print("Hello", name)

# Call the function with multiple names
greet_all("Alice", "Bob", "Charlie")

# Define a lambda function to add two numbers
add = lambda num1, num2: num1 + num2

# Call the lambda function and print the result
print(f"The sum of 3 and 5 is {add(3, 5)}")
