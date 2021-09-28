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
P = li_int_sp()
Q = [0]*N
for i, p in enumerate(P, 1):
    Q[p-1] = i
print(*Q)