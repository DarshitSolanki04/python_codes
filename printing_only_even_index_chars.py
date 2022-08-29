sentence = input('Type a word: ')
print('\n')
print('Original String is', sentence)

size = len(sentence)

print('\n')
print('Printing only even index chars:')

for i in range(0, size, 2):
    print(sentence[i], end=' ')
print('\n')  # 'print()' added to make the prompt appear in the new line while executing the command through terminal.
