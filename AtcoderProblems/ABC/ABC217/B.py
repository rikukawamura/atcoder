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
lists = ['ABC', 'ARC', 'AGC', 'AHC']
S1 = input()
S2 = input()
S3 = input()
del lists[lists.index(S1)]
del lists[lists.index(S2)]
del lists[lists.index(S3)]
print(*lists)
