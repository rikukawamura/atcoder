def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from bisect import bisect_left
H, W, N = int_sp()
A = []
B = []
ori = []
for _ in range(N):
    a, b = int_sp()
    A.append(a)
    B.append(b)
    ori.append([a,b])
A = list(set(A))
B = list(set(B))
A.sort()
B.sort()
#pdb.set_trace()

for a, b in ori:
    print(bisect_left(A, a)+1, bisect_left(B, b)+1)
    