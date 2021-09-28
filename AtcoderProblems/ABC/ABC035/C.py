def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from itertools import accumulate

N, Q = int_sp()
x = [0]*(N+1)
for _ in range(Q):
    l, r = int_sp()
    x[l-1] += 1
    x[r] += -1

x = list(accumulate(x))
y = []
for i in x[:-1]:
    y.append(str(i%2))
print(''.join(y))