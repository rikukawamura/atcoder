def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

import pdb
import math
N = int(input())
str_N = str(N)
len_N = len(str(N))
total = 0
if len_N == 1:
    total += 1
elif len_N == 2:
    # 1点の場合
    total += 1
    total += 1*int(str_N[1])
    # 2点の場合
    if N >= 11:
        total += 2
elif len_N == 3:
    # 1点の場合
    total += 1
    total += 1*(int(str_N[1])-1)*10
    total += 1*int(str_N[2]+1)
    # 2点の場合
    total += 2*


