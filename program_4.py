# Appends odd numbers from list1 to lst and even numbers from list2 to lst.


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

lst = []

for i in list1:
    if i % 2 != 0:
        lst.append(i)

for i in list2:
    if i % 2 == 0:
        lst.append(i)

print('Resulting list:', lst)

