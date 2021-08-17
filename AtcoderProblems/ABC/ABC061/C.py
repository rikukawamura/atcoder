def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from collections import defaultdict

N, K = int_sp()
x = defaultdict(int)

for _ in range(N):
    a, b = int_sp()
    x[a] += b
x = sorted(x.items(), key=lambda x:x[0])
total = 0
for key, value in x:
    total += value
    if total >= K:
        print(key)
        exit()

