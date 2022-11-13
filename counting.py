'''
Counts how many times a particular word/fragment has  appeared in a string.
'''

var = input('Type a sentence: ')  # e.g. Emma is a good developer. Emma is a writer.
n = input('Type a word: ')  # Program is case-sensitive.
cnt = var.count(n)

print(f'{n} appeared {cnt} times.')
