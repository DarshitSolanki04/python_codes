sta = input('Type a word: ')
print('\nOriginal String is', sta)

size = len(sta)

print('\nPrinting only even index chars:')

for i in range(0, size, 2):
    print(sta[i], end=' ')
