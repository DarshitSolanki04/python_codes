# Prints the sum of every 2 consecutive numbers in a given range.


print('Printing the sum of every 2 consecutive numbers in range(10)')  # Remember, in range(10) the number 10 is not included.

prev_number = 0 

for curr_number in range(10):  # Initially both the numbers are same, i.e. zero.
    # print('Current Number', i, ' Previous Number', j, ' Sum:', i+j)
    print('Current Number %d Previous Number %d Sum: %d' % (curr_number, prev_number, curr_number+prev_number))
    prev_number = curr_number

