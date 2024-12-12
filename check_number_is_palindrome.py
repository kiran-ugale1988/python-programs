'''
Q5. Design a code which will find the given number is Palindrome number or not.
Hint: Use built-in functions of string.
'''
# Function to check if a number is a palindrome
def is_palindrome(number):
    # Convert the number to a string
    num_str = str(number)
    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]

# Input number
number = input("Enter a number: ")

# Check if the number is a palindrome
if is_palindrome(number):
    print(f"{number} is a palindrome number.")
else:
    print(f"{number} is not a palindrome number.")

'''
o/p:
check_number_is_palindrome.py 
Enter a number: 121
121 is a palindrome number.

'''
'''
check_number_is_palindrome.py 
Enter a number: 14455
14455 is not a palindrome number.
'''