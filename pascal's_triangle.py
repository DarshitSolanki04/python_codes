# Pascal's Triangle


def pascal_line(array):
    line = []
    line.append(1)
    for i in range(len(array)-1):
        line.append(array[i] + array[i+1])
    line.append(1)
    return line


n = int(input('Number of Lines: '))

if n < 1:
    print('Type a number greater than 0.')
elif n == 1:
    print(1)
else:
    print(1)
    print(1, 1)
    printer = [1, 1]
    for i in range(n - 2):
        printer = pascal_line(printer)
        for j in printer:
            print(j, end=' ')
        print('')
