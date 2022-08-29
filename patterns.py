import sys


print('''Type two integers separated by a space. The first integer should be an
odd number while the second integer should be three times the first
integer:\n''')

n, m = map(int, input().split())

if n % 2 == 0 or m != 3 * n:
    print('The conditions are not met. Try again.')
    sys.exit()

print('\n')

for i in range((n-1)//2):
    print(('.|.'*(2*i+1)).center(m, '-'))

print('WELCOME'.center(m, '-'))

for i in range((n-3)//2, -1, -1):
    print(('.|.'*(2*i+1)).center(m, '-'))
