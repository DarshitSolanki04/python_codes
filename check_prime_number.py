n = int(input('Enter a number: '))

x = 0

if n > 1:
    for i in range(2, n):
        if n % i != 0:
            x += 1
            continue

        print(n, 'is not a prime number.')
        break

    if x == n - 2:
        print(n, 'is a prime number.')
else:
    print(n, 'is not a prime number.')
