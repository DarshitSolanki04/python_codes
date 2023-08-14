# Prints the product of two integers if their product is less than 1000 otherwise it prints their sum.

# input() function always returns a string. We have to type cast it as an integer using int() to use it later in arithmetic equations.
num1 = int(input('number1 = '))
num2 = int(input('number2 = '))

if num1*num2 < 1000:
    print('\nThe result is', num1*num2)  # \n prints a new line before "The result"
else:
    print('\nThe result is', num1+num2)
