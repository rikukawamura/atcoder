def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from collections import defaultdict
import copy

N = int(input())
A = li_int_sp()
A.sort()
B = defaultdict(int)

for a in A:
    B[a] += 1
keys = B.keys()
C = copy.deepcopy(B)

for a in A:
    pdb.set_trace()
    if a*2 in keys:
        del C[a]

print(len(C))