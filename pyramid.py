n = int(input('Type an integer: '))

for i in range(1, n+1):
    for j in range(i):
        print(i, end=' ')
    print('\n')
