import pdb
from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))
A_acc = list(accumulate(A))

min_val = float('INF')
for i in range(N-1):
    tmp = abs(A_acc[i] - (A_acc[N-1]-A_acc[i]))
    min_val = min(tmp, min_val)
print(min_val)
