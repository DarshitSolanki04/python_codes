"""
Checks whether the input number is an armstrong number or not.

Armstrong number is a number in which when each digit is raised to the power of the total number of digits in the original number and summed then it returns the same original number. e.g.: 8208 -> 8^4 + 2^4 + 0^4 + 8^4 = 8208.
"""


n = int(input("Enter a number: "))

x = n
t = n

cnt = 0
z = 0

while x > 0:  # This loop finds the total no. of digits in the input number.
    x = x // 10
    cnt += 1


while t > 0:  # This loop finds the sum of all the digits raised to cnt.
    r = t % 10
    z = z + r**cnt
    t = t // 10


if z == n:
    print("The given no. is an armstrong number.")
else:
    print("The given no. is not an armstrong number.")
