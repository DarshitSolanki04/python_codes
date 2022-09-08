# Pascal's Triangle

P = [1]
Q = [1, 1]

n = int(input('Number of Lines: '))

print(P)
print(Q)

P = []

for i in range(2, n):
    P.append(1)
    for j in range(1, i):
        P.insert(j, Q[j-1] + Q[j])
    P.append(1)
    print(P)
    Q = P.copy()
    P = []

