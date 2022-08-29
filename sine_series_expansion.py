import math

o = int(input('Enter the value of theta (in deg): '))
n = int(input('Enter the no. of approximation terms: '))

theta = o * math.pi / 180

z = 0

for i in range(n):
    z = z + ((-1)**i * theta**(2*i+1)) / math.factorial(2*i+1)

print('\nsin(', o, ') =', z)
