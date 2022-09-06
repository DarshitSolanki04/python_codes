# Multiplication table from 1 to 10.


for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end=' ')
        # print("{:<3}".format(i*j), end =' ')  # Advanced: This line formats the spacing in output so that the result looks good.
    print('\n')
