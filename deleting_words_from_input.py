var = input('Type a word: ')

x = int(input('Type the no. of words you want to remove: '))
print('')

size = len(var)

for i in range(x, size):
    print(var[i], end='')
