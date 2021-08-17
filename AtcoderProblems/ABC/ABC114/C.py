def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from itertools import product
from collections import Counter
from bisect import bisect_right

N = int(input())
pos_sel = []
total = 0
for i in range(3, 11):
    for j in product(['7', '5', '3'], repeat=i):
        total += len(j)
        if len(Counter(j)) >= 3:
            pos_sel.append(int(''.join(j)))
pdb.set_trace()
pos_sel = sorted(pos_sel)
th = bisect_right(pos_sel, N)
print(th)