'''
Q4.Write a program that accepts a sentence and calculate the number of letters and
digits.
'''
# Function to count letters and digits in a sentence
def count_letters_and_digits(sentence):
    letters = 0
    digits = 0

    for char in sentence:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1

    return letters, digits

# Input sentence
sentence = input("Enter a sentence:")

# Count letters and digits
letters, digits = count_letters_and_digits(sentence)

# Print the result
print(f"LETTERS: {letters}")
print(f"DIGITS: {digits}")

'''
count_letters_and_digits.py 
Enter a sentence:Python0325
LETTERS: 6
DIGITS: 4

'''

'''
count_letters_and_digits.py 
Enter a sentence: this is kiran
LETTERS: 11
DIGITS: 0
'''

'''
count_letters_and_digits.py 
Enter a sentence: this kiran and my birth year is 1988
LETTERS: 25
DIGITS: 4
'''