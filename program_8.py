"""
This program prints an upside down right-angled triangle.
* * * * *
* * * *
* * *
* *
*
"""


for i in range(5, 0, -1):  # Here we dictate that the loop starts from 5 and ends with 1 in -1 increments.
    for j in range(i):
        print('*', end=' ')
    print('')  # Prints a new line as by default, end='\n'.
