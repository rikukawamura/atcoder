import pdb
import numpy as np
import itertools

N, K = map(int, input().split())
H = [int(input()) for _ in range(N)]
H = sorted(H)

max_val = float('INF')

#添字の範囲を考えるのはめんどくさかったから，try-except文を使用
for i in range(N):
    try:
        tmp = H[i+K-1]-H[i]
        max_val = min(tmp, max_val)
    except:
        break
print(max_val)
