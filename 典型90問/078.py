def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from collections import defaultdict

N, M = int_sp()
A, B = [], []
total = defaultdict(int)
for _ in range(M):
    a, b = int_sp()
    if a < b:
        total[b] += 1
    else:
        total[a] += 1

cnt = 0
for key, value in zip(total.keys(), total.values()):
    if value == 1:
        cnt += 1
print(cnt)




