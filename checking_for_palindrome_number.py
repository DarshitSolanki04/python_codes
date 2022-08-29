x = 0

z = input('Type a number: ')

R = len(z)

for i in range(R//2):
    if z[i] == z[- (i+1)]:
        x += 1

if x == R//2:
    print('Yes. The given number is a palindrome number.')
else:
    print('No. The given number is not a palindrome number.')
