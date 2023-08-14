# This program reverses a given integer.

n = int(input('Enter a number: '))

print('Result:', end=' ')

while n > 0:
    r = n % 10  # n % 10 outputs the last digit of an integer, i.e. 3241 % 10 = 1, 459 % 10 = 9 etc.
    print(r, end='')  # end='' is added to avoid the function printing a new line. By default, end='\n' which prints a new line. 
    n = n // 10  # n // 10 will output the floor (the closest lower integer) of the result, i.e. 3.4 // 1 = 3, 3.9 // 1 = 3, 3241 // 10 = 324, etc.
