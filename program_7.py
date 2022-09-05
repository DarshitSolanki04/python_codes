# Multiplication table from 1 to 10.

for i in range(1, 11):
    for j in range(1, 11): #this loop goes 1 through 10 before the first loop increases by 1.
        print(i*j, end=' ')
        #print("{:<3}".format(i*j), end =' ')  advanced: this line formats the spacing in output to look good.
    print('\n')
