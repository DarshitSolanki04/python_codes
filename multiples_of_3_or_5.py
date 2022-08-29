# Multiples of 3 and 5
# Project Euler - Prb 1

t = int(input().strip())
for i in range(t):
    my_list3 = [0]
    my_list5 = [0]
    my_list15 = [0]
    n = int(input().strip())
    for j in range(n-1, 1, -1):
        k = list(map(int, str(j)))
        if sum(k) % 3 == 0:
            my_list3[0] = j
            break
    for j in range(n-1, 1, -1):
        k = list(map(int, str(j)))
        if k[-1] % 5 == 0:
            my_list5[0] = j
            break
    for j in range(n-1, 1, -1):
        k = list(map(int, str(j)))
        if sum(k) % 3 == 0 and k[-1] % 5 == 0:
            my_list15[0] = j
            break

    n3 = int(my_list3[0] / 3)
    n5 = int(my_list5[0] / 5)
    n15 = int(my_list15[0] / 15)

# The use of bitwise operator is very important here because the following
# calculation can involve numbers of the order of 10^9 can multiplying
# big numbers and dividing by 2 can create very large inaccuracies. Therefore,
# when multiplying and dividing by 2 use bitwise operators.

    ans = ((n3*3*(n3+1)) >> 1) + ((n5*5*(n5+1)) >> 1) - ((n15*15*(n15+1)) >> 1)
    print(int(ans))
