def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
import queue
from collections import defaultdict, Counter

N, X, Y = int_sp()
X = X-1
Y = Y-1
cnt = [0]*(N-1)

for i in range(N-1):
    for j in range(i+1, N):
        x = abs(j-i)
        y = abs(i-X)+1+abs(Y-j)
        min_val = min(x, y)
        cnt[min_val-1] += 1

for i in cnt:
    print(i)







