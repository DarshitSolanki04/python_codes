n = int(input('Enter a number: '))

x = n
t = n

nod = 0
z = 0

while x > 0:
    x = x // 10  # This loop finds the total no. of digits in the input number.
    nod += 1


while t > 0:
    r = t % 10
    z = z + r ** nod  # This loop finds the sum of cube of each digit.
    t = t // 10


if z == n:
    print('The given no. is an armstrong number.')
else:
    print('The given no. is not an armstrong number.')
