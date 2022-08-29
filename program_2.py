print('Printing current and previous number sum in a range(10)')

j = 0

for i in range(10):
    # print('Current Number', i, ' Previous Number', j, ' Sum:', i+j)
    print('Current Number %d Previous Number %d Sum: %d' % (i, j, i+j))
    j = i
