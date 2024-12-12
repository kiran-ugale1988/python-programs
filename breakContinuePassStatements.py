for number in range(1, 11):
    if number == 5:
        break
    print(number)
print("Loop exited because break was called.")
'''
1
2
3
4
Loop exited because break was called.
'''

for number in range(1, 11):
    if number == 5:
        continue
    print(number)
print("Loop finished with continue.")
'''
1
2
3
4
6
7
8
9
10
Loop finished with continue.
'''

for number in range(1, 11):
    if number == 5:
        pass
    print(number)
print("Loop finished with pass.")

def some_function():
    pass  # Function implementation will be added later

class SomeClass:
    pass  # Class implementation will be added later

print("pass used as placeholder or used like we dont want to write code inside it now but code should work.")

'''
Loop finished with pass.
pass used as placeholder or used like we dont want to write code inside it now but code should work.
'''
