a = 10
b = 5

a = a + b
print(a)
a = 10
a = a - b
print(a)
a = 10
a = a * b
print(a)
a = 10
a = a / b
print(a)
a = 10
a = a % b
print(a)
a = 10
a = a // b
print(a)
print('\n')
a = 10
b = 5
res = a and b
print(res)  # Output: 5
'''
and Operator:
The and operator returns the first falsy value or the last value if none are falsy. In Python, non-zero numbers are considered True and zero is False. Here’s how the and operator works with a and b:

a is 10, which is True.

b is 5, which is True.

Since both a and b are True, a and b evaluates to the last True value, which is b (5).
'''
res = a or b
print(res)  # Output: 10
'''
or Operator:
The or operator returns the first truthy value or the last value if none are truthy. Here’s how the or operator works with a and b:

a is 10, which is True.

b is 5, which is True.

Since a is already True, a or b evaluates to the first True value, which is a (10).

or -> always returns the higher value
and -> always returns the lower value
'''

print('\n')
'''
Identity Operators
Identity operators are used to compare the memory locations of two objects. There are two identity operators: is and is not.

is: Evaluates to True if the variables on either side of the operator point to the same object in memory.

is not: Evaluates to True if the variables on either side of the operator do not point to the same object in memory.
'''
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)   # True, because b is the same object as a
print(a is c)   # False, because c is a different object with the same content
print(a is not c)  # True, because a and c are different objects
print('\n')

'''
Membership Operators
Membership operators are used to test if a value is a member of a sequence (like a list, tuple, string, etc.). There are two membership operators: in and not in.

in: Evaluates to True if the specified value is found in the sequence.

not in: Evaluates to True if the specified value is not found in the sequence.
'''
numbers = [1, 2, 3, 4, 5]

print(3 in numbers)       # True, because 3 is in the list
print(6 in numbers)       # False, because 6 is not in the list
print(6 not in numbers)   # True, because 6 is not in the list


'''
o/p:
15
5
50
2.0
0
2

5
10

True
False
True

True
False
True

'''