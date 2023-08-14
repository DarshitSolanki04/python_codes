"""
Checks whether the input number is an armstrong number or not.
"""


n = input('Type a positive integer: ')

num_of_digits = len(n)
m = int(n)

num = 0

if m < 0:
    print(m, 'is not an Armstrong number.')
else:
    for i in range(num_of_digits):
        num += (m % 10) ** num_of_digits
        m = int(m / 10)
    
    if int(n) == num:
        print(n, 'is an Armstrong number.')
    else:
        print(n, 'is not an Armstrong number.')
