import pdb
import collections

N = int(input())
A = [int(input()) for _ in range(N)]
A_col = collections.Counter(A)

count = 0
for key, val in zip(A_col.keys(), A_col.values()):
    if val % 2 == 1:
        count += 1

print(count)

