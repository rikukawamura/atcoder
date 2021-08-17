def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from collections import Counter

N = int(input())
A = li_int_sp()
A = Counter([x%4 for x in A])
#pdb.set_trace()

x, y = 0, 0
for key, value in zip(A.keys(), A.values()):
    if key == 2:
        y += value % 2
    elif key == 0:
        x += value
    else:
        y += value
if y <= x:
    print('Yes')
else:
    if y-x == 1:
        print('Yes')
    else:
        print('No')

