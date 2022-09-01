'''
Prints all the elements of a list that are divisible by 5.
'''


def divisible_by_5(array):

    print('Given list:', array, '\n')
    print('Divisible by 5:')

    for i in array:
        if i % 5 == 0:
            print(i)


list1 = [101, 205, 335, 46, 55, 105]

divisible_by_5(list1)

