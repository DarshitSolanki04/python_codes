'''
Binary search program.
'''

x_low = int(input())
x_high = int(input())

while True:
    diff = x_high - x_low
    print(int(x_low + diff//2))
    if input() == 'l':
        x_low = int(x_low + diff//2 + 1)
    else:
        x_high = int(x_low + diff//2 - 1)
