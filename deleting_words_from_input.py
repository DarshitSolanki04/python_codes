'''
Removes the first 'n' characters from the input word.
'''


var = list(input('Type any word: '))

n = int(input('Type the no. of characters you want to remove: '))

if n > len(var):
    print('The number can not be greater then the length of the input word.')
else:
    print(''.join(var[n:]))
