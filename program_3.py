def fls(lst):
    print('\nGiven lst:', lst)

    num1 = lst[0]
    num2 = lst[-1]

    if num1 == num2:
        return True

    return False


lst1 = [10, 20, 30, 40, 10]
print('result is', fls(lst1))

lst2 = [75, 65, 35, 75, 30]
print('result is', fls(lst2))

print(fls(lst2))
