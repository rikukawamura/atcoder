def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


import pdb

N = int(input())
C = li_int_sp()
mod = 10**9+7

total = 1
C = sorted(C)
for i, c in enumerate(C):
    x = c-i
    total *= (x%mod)

print(total%mod)