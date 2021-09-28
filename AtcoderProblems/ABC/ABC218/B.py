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
P = li_int_sp()
al = 'abcdefghijklmnopqrstuvwxyz'
total = []
for p in P:
    total.append(al[p-1])

print(''.join(total))
