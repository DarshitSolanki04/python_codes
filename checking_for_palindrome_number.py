# Checks if the input number is a palindromic number or not.
# A palindromic number is a number that remains the same when its digits are reversed. eg: 121, 3456543, etc.

n = input('Type a number: ')

size = len(n)

for i in range(size//2):
    if n[i] == n[-(i+1)]:
        continue
    else:
        print('No, the given number is not a palindrome number.')
        break
else:
    print('Yes, the given number is a palindrome number.')

