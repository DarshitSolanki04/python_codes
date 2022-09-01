# Prints the product of two integers if their product is less than 1000 otherwise it prints their sum.


num1 = int(input('number1 = '))
num2 = int(input('number2 = '))

if num1*num2 < 1000:
    print('\nThe result is', num1*num2)
else:
    print('\nThe result is', num1+num2)

