import pdb
import collections

N = int(input())
A = list(map(int, input().split()))
A_col = collections.Counter(A)

del_count = 0
for key, val in zip(A_col.keys(), A_col.values()):
    if val >= key:
        del_count += val - key
    else:
        del_count += val
print(del_count)
