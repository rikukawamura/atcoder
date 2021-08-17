def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from math import log
from bisect import bisect_left, bisect_right

N = int(input())
A = sorted(li_int_sp())
B = sorted(li_int_sp())
C = sorted(li_int_sp())

total = 0
for b in B:
    a = bisect_left(A, b)
    c = N-bisect_right(C, b)
    total += a*c
print(total)



