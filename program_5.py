# This program reverses a given integer.

n = int(input('Enter a number: '))

print('Result:', end=' ')

while n > 0:
    r = n % 10       # n%10 will always output the last digit in an integer. i.e. 3241%10 = 1 , 459%10 = 9.
    print(r,end='')  # end='' is added to avoid the program printing a new line. By default, end='\n' which prints a new line. 
    n = n // 10      # n//10 will do the same as n/10 but the result will be an integer. i.e. 3241//10 = 324 instead of 324.1.
