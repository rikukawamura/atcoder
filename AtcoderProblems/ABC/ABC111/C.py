import pdb
import collections

N = int(input())
V = list(map(int, input().split()))
V_col = collections.Counter(V)
V_col = sorted(V_col.items(), key=lambda x:x[1], reverse=True)
min_val = sum([x[1] for x in V_col[2:]])
print(min_val)