'''
test.txt :

5 6
1 2 3 4
5 6 7 8
'''

with open('test.txt', 'r') as file:
    lines = file.readlines()

n, m = map(int, lines[0].split())
N = list(map(int, lines[1].split()))  # or use set(); much faster
M = list(map(int, lines[2].split()))
