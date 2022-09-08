'''
Expansion of sine of theta.
'''


import math

angle = int(input('Enter the value of theta (in deg): '))
no_of_terms = int(input('Enter the no. of approximation terms: '))

theta = angle * math.pi / 180

z = 0

for i in range(no_of_terms):
    z = z + ((-1)**i * theta**(2*i+1)) / math.factorial(2*i+1)

print('\nsin(', angle, ') =', z)

