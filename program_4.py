lst1 = [10, 20, 25, 30, 35]
lst2 = [40, 45, 60, 75, 90]

lst = []

for i in lst1:
    if i % 2 != 0:
        lst.append(i)

for i in lst2:
    if i % 2 == 0:
        lst.append(i)

print('\nResulting list:', lst)
