import pdb
from itertools import accumulate
import numpy as np


N = int(input())
A = list(map(int, input().split()))
sei = [x if x < 0 else 0 for x in A]
not_sei = [x if x >= 0 else 0 for x in A]


tmp1 = accumulate(A)
now = [0] + list(accumulate(tmp1))

tmp2 = 0
val = 0
max_val = -float('INF')
for i, j in zip(now, A):
    pdb.set_trace()
    if j > 0:
        val = now + j
    if val > max_val:
        max_val = val
    
    
