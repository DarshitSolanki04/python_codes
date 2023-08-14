'''
Prints a list of numbers divisible by 5 from the given input.
'''


array = list(map(int, input('Type an array of numbers separated by a space: ').split()))

print([i for i in array if ((i % 10) == 0 or (i % 10) == 5)])
