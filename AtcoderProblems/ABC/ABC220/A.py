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

A, B, C = li_int_sp()
for i in range(A, B+1):
    if i%C == 0:
        print(i)
        exit()
print(-1)