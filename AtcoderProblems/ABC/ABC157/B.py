import pdb
import numpy as np
import itertools
a = [list(map(int, input().split())) for _ in range(3)]
a = np.array(a)
a_t = a.T
a_slope = []
a_s = []
a_s.append(a[0][0])
a_s.append(a[1][1])
a_s.append(a[2][2])
a_slope.append(a_s)
a_s = []
a_s.append(a[0][2])
a_s.append(a[1][1])
a_s.append(a[2][0])
a_slope.append(a_s)
bingo = []
for i in a:
    bingo.append(i.tolist())
for i in a_t:
    bingo.append(i.tolist())
for i in a_slope:
    bingo.append(i)
n = int(input())
b = [int(input()) for _ in range(n)]

flag = False
for i in bingo:
    for k, j in enumerate(i):
        if j not in b:
            break
        elif k == 2:
            flag = True
if flag:
    print('Yes')
else:
    print('No')
