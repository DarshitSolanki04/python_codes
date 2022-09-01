'''
Checks if the input number is a palindromic number or not.

A palindromic number is a number that remains the same when its digits are reversed. e.g.: 121, 3456543, etc.
'''


n = input('Type a number: ')

size = len(n)

for i in range(size//2):  # In python, you can use 'for-else' loop. The 'else' loop is executed only if the 'for' loop completes fully if it breaks in-between the 'else' loop is skipped.
    if n[i] == n[-(i+1)]:
        continue
    else:
        print('No, the given number is not a palindrome number.')
        break
else:
    print('Yes, the given number is a palindrome number.')

