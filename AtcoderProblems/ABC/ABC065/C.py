def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from math import factorial

N, M = int_sp()
mod = 10**9+7
if abs(N-M) > 1:
    print(0)
    exit()
else:
    if N == M:
        print((factorial(N)%mod*factorial(M)%mod*2)%mod)
    else:
        print((factorial(N)%mod * factorial(M)%mod)%mod)