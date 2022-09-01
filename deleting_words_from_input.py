'''
Removes the given number of characters from the input word from the begining.
'''


var = input('Type a word: ')

n = int(input('Type the no. of characters you want to remove: '))
print('')

size = len(var)

for i in range(n, size):
    print(var[i], end='')
print('\n')

