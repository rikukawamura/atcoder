import pdb
from itertools import accumulate
import numpy as np


N = int(input())
A = list(map(int, input().split()))
sei = [x if x > 0 else 0 for x in A]
sei_acc = list(accumulate(sei))
A_acc = list(accumulate(A))

pdb.set_trace()
max_val = -float('INF')
now = 0
for x, y in zip(sei_acc, A_acc):
    max_val = max(max_val, now+x)
    now += y
print(max_val)

    
