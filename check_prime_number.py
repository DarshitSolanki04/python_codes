'''
This is a straight forward code to check if a number is a prime number or not.

Note: This code is not efficient for checking very big prime numbers.
'''


n = int(input('Enter a number: '))

if n > 1:  # All prime numbers are greater than one. Note: One is not a prime number.
    for i in range(2, n):  # In python, you can use 'for-else' loop. The 'else' loop is executed only if the 'for' loop completes fully if it breaks in-between the 'else' loop is skipped.
        if n % i == 0:
            print(n, 'is not a prime number.')
            break
    else:
        print(n, 'is a prime number.')
else:
    print(n, 'is not a prime number.')

