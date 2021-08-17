def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from collections import defaultdict

N, K = int_sp()
C = li_int_sp()
color = defaultdict(int)

for i in range(K):
    color[C[i]] += 1
if N == K:
    print(len(color))
    exit()

max_val = len(color)

for i in range(N-K):
    color[C[i]] -= 1
    color[C[i+K]] += 1
    if color[C[i]] == 0:
        del color[C[i]]
    max_val = max(max_val, len(color))
print(max_val)
