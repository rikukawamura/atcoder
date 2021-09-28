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
import copy
import numpy as np
N = int(input())
tmpS = [input() for _ in range(N)]
tmpT = [input() for _ in range(N)]
#pdb.set_trace()

S = []
T = []
for s, t in zip(tmpS, tmpT):
    if '#' in s:
        S.append(s)
    if '#' in t:
        T.append(t)
#pdb.set_trace()

S = list(map(list, (zip(*S))))
T = list(map(list, (zip(*T))))

S2 = []
T2 = []
for s, t in zip(S, T):
    if '#' in s:
        S2.append(s)
    if '#' in t:
        T2.append(t)
S2 = np.array(S2)
T2 = np.array(T2)
#pdb.set_trace()

for _ in range(4):
    #pdb.set_trace()
    if S2.shape == T2.shape:
        if (S2 == T2).all():
            print('Yes')
            exit()
    T2 = np.rot90(T2)
print('No')






