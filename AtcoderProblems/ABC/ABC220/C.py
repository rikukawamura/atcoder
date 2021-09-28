def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)

import pdb
import math
N = int(input())
A = li_int_sp()
X = int(input())
sum_A = sum(A)
waru = X//sum_A
amari = X %sum_A
#pdb.set_trace()

total = 0
for i, a in enumerate(A, 1):
    total += a
    if total > amari:
        print((waru*N)+i)
        exit()