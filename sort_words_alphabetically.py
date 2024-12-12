'''
Q2. Write a code which accepts a sequence of words as input and prints the words in a
sequence after sorting them alphabetically.
'''
#accept the sequence of words as input
input_words = input("Enter the words separate by spaces:")

words_list = input_words.split()

sorted_words = sorted(words_list)

print("sorted words: ", sorted_words)

'''
o/p:
sort_words_alphabetically.py 
Enter the words separate by spaces:ugale kiran
sorted words:  ['kiran', 'ugale']

'''
