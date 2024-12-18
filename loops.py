numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
'''
1
2
3
4
5
'''

count = 99
while count >= 95:
    print(count)
    count -= 1
'''
99
98
97
96
95
'''

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} * {j} = {i * j}")
    print("-" * 10)

'''
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
----------
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
----------
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
----------
4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
4 * 4 = 16
4 * 5 = 20
----------
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
----------
'''