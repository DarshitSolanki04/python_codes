'''
Checks if the input number is a palindromic number or not.
'''


n = list(input('Type a positive integer: '))

m = n.copy()
m.reverse()

num_n = ''.join(n)
num_m = ''.join(m)

if int(num_n) < 0:
    print(num_n, 'is not a Palindrome number.')
else:
    if num_n == num_m:
        print(num_n, 'is a Palindrome number.')
    else:
        print(num_n, 'is not a Palindrome number.')
