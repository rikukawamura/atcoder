import pdb
import collections
import itertools


N = int(input())
A = list(map(int, input().split()))
A_col = collections.Counter(A)

total = 0
for value in A_col.values():
    total += (value * (value-1)) // 2

for a in A:
    diff = total - (A_col[a]-1)
    print(diff)
