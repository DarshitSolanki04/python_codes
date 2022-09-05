# Prints the sum of every 2 consecutive numbers in a given range.


print('Printing the sum of every 2 consecutive numbers in range(10)')  # Remember, in range(10) the number 10 is not included.

prevNumber = 0 

for currNumber in range(1,10):  # We start from initial value 1 in the current number because the previous number is already a 0.
    # print('Current Number', i, ' Previous Number', j, ' Sum:', i+j)
    print('Current Number %d Previous Number %d Sum: %d' % (currNumber, prevNumber, currNumber+prevNumber))
    prevNumber = currNumber

