def db5(lst):
    print('Given list:', lst)
    print('\nDivisible by 5:')

    for i in lst:
        if i % 5 == 0:
            print(i)


lst1 = [101, 205, 335, 46, 55, 105]
db5(lst1)
