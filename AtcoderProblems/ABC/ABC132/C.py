import pdb
import collections as col
import itertools as iter

n = int(input())
d = list(map(int, input().split()))
d_col = dict(col.Counter(d))
d_col = sorted(d_col.items())
d_val = [x[1] for x in d_col]
d_val_acc = list(iter.accumulate(d_val))

flag = False
for i in range(len(d_val)-1):
    if d_val_acc[i] == d_val_acc[-1]-d_val_acc[i]:
        flag = True
        break
if flag:
    print(d_col[i+1][0]-d_col[i][0])
else:
    print(0)
