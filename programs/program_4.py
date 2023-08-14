# Appends odd numbers from list1 to lst and even numbers from list2 to lst.


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

lst = []

for i in list1:  # Remember, here 'i' take 'values' from list1, it is not an index. i.e. the first value of i will be 10 not 0.
    if i % 2 != 0:  # i % 2 will calculate the remainder of division (i/2), if it is not equal to 0 that means we have an odd number.
        lst.append(i)  # Remember, 'append()' adds an element at the end of the list.

for i in list2:
    if i % 2 == 0:
        lst.append(i)

print('Resulting list:', lst)
