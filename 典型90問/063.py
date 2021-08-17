def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from collections import Counter


H, W = int_sp()
grid = [li_int_sp() for _ in range(H)]
max_val = 0

for bit in range(2**H):
    temp = []
    temp2 = []
    for i in range(H): # H個の行をbit全探索．
        if 1 & (bit >> i):
            temp.append(grid[i])

    for i in list(map(list, (zip(*temp)))): #
        if len(set(i)) == 1:
            temp2.append(i[0])

    for j in Counter(temp2).values():
        max_val = max(j*len(i), max_val)
print(max_val)



