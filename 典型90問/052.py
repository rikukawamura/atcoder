def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from itertools import product

N = int(input())
total = 1
mod = 10**9+7
for _ in range(N):
    A = li_int_sp()
    total *= sum(A)
print(total%mod)
