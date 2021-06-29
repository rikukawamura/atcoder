from math import factorial

def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))


def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

import pdb
from collections import Counter

N = int(input())
A = li_int_sp()
A = Counter(A)
all_comb = comb(N, 2)
total = 0
for key, value in zip(A.keys(), A.values()):
    if value > 1:
        total += comb(value, 2)
print(all_comb-total)

