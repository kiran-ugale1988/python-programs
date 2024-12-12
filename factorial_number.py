'''
Q1. Write a program which will find factors of given number and find whether the
factor is even or odd.
'''
#function to find factors and determine if they are even or odd
def find_factors_and_check_parity(n):
    #loop through all numbers from 1 to n
    for i in range(1, n+ 1 ):
        #check if i is factor of n
        if n % i == 0:
            #deternmine if the factor is even or odd
            if i % 2 == 0:
                print(f"Factor {i} is even")
            else:
                print(f"Factor {i} is odd")


#input number
number = int(input("Enter a number to find factors and its parity:"))

find_factors_and_check_parity(number)

'''
o/p:
python factorial_number.py   
Enter a number to find factors and its parity:15
Factor 1 is odd
Factor 3 is odd
Factor 5 is odd
Factor 15 is odd
'''
'''
python factorial_number.py
Enter a number to find factors and its parity:12
Factor 1 is odd
Factor 2 is even
Factor 3 is odd
Factor 4 is even
Factor 6 is even
Factor 12 is even

'''
