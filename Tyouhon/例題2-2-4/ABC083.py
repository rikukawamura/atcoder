import pdb

x, y = map(int, input().split())

init = x
row = []
while init <= y:
    row.append(init)
    init *= 2
print(len(row))