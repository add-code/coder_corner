# Import the os module for file deletion
import os

# Open and read a file
def read_file(filename):
    with open(filename, 'r') as file:
        print(file.read())

# Write to a file
def write_file(filename):
    with open(filename, 'w') as file:
        file.write('Hello, world!\n')

# Write multiple lines to a file
def write_lines(filename):
    with open(filename, 'w') as file:
        lines = ['Hello, world!\n', 'Welcome to Python file handling.\n']
        file.writelines(lines)

# Append to a file
def append_file(filename):
    with open(filename, 'a') as file:
        file.write('This is an appended line.\n')

# Delete a file
def delete_file(filename):
    if os.path.isfile(filename):
        os.remove(filename)
    else:
        print('Error: File not found.')

# Test the functions
def main():
    filename = 'myfile.txt'
    write_file(filename)
    append_file(filename)
    read_file(filename)
    delete_file(filename)

# Run the main function
if __name__ == '__main__':
    main()
