# Prints the sum of current and previous number in a given range.


print('Printing the sum of current and previous number in range(10)')  # Remember, in range(10) the number 10 is not included.

j = 0

for i in range(10):  # Initially both the numbers are same, zero.
    # print('Current Number', i, ' Previous Number', j, ' Sum:', i+j)
    print('Current Number %d Previous Number %d Sum: %d' % (i, j, i+j))
    j = i

