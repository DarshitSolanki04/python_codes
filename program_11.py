'''
Prints (if n = 3)
1 1 1
2 2
3
'''


n = int(input('Enter the no. of rows: '))
x = 1

for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(x, end=' ')
    print()
    x += 1

