'''
Command line arguments allow users to provide input parameters to a program
when they execute it from the terminal. In Python,
you can access command line arguments using the sys module
or the argparse module for more complex parsing.

Using the sys Module
Example: Let's create a simple Python script that takes two command line arguments
(a name and an age) and prints a message.
'''

import sys

print(len(sys.argv))

print(sys.argv)

# Check if the right number of arguments are provided
if len(sys.argv) != 3:
    print("Usage: python script.py <name> <age>")
    sys.exit(1)

# Extract the command line arguments
name = sys.argv[1]
age = sys.argv[2]

print(f"Hello, {name}! You are {age} years old.")

'''
o/p:
PS \PythonCourseEdureka> python argumentexample.py 1234 kiran 
3
['.\\argumentexample.py', '1234', 'kiran']
Hello, 1234! You are kiran years old.
'''