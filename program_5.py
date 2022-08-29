n = int(input('Enter a number: '))

print('Result:', end=' ')

while n > 0:
    r = n % 10
    print(r, end=' ')
    n = n // 10
