def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from collections import defaultdict

N = int(input())
A = li_int_sp()
B = defaultdict(int)
A.sort()

i = 0
for a in A:
    if a/2 in B.keys():
        B[a] = B[a/2]
    else:
        B[a] = i
        i+=1
print(len(set(B.values())))