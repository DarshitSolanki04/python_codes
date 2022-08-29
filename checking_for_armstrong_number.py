n = int(input('Enter a number: '))

x = n
t = n

nod = 0
z = 0

while x > 0:  # This loop finds the total no. of digits in the input number.
    x = x // 10
    nod += 1


while t > 0:  # This loop finds the sum of all the digits raised to nod.
    r = t % 10
    z = z + r ** nod
    t = t // 10


if z == n:
    print('The given no. is an armstrong number.')
else:
    print('The given no. is not an armstrong number.')

