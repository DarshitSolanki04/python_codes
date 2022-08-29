n = int(input('Enter income to calculate tax: '))

if n <= 10000:
    print('\nIncome is not taxable.')
elif n <= 20000:
    x = n - 10000
    y = x / 10
    print('\nPayable tax amount:', y)
else:
    x = n - 20000
    y = x / 5 + 1000
    print('\nPayable tax amount:', y)
