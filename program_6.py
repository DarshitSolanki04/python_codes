# This program calculates taxes based on income

income = int(input('Enter income to calculate tax: '))

if income <= 10000:
    print('\nIncome is not taxable.')
elif income <= 20000:
    tax = (income - 10000)/10
    print('\nPayable tax amount:', tax)
else:
    tax = (income - 20000)/5 + 1000
    print('\nPayable tax amount:', tax)
