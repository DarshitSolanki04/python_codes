'''
Python code to check prime numbers.
'''

import math


n = int(input('Type a positive integer: '))

if (n < 0):
    print('Negative numbers can not be prime. Please type a positive integer.')
elif (0 <= n < 2):
    print(n, 'is not a prime number.')
else:
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            print(n, 'is not a prime number.')
            break
    else:
        print(n, 'is a prime number.')
