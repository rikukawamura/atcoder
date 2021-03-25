import pdb
import itertools
import collections
import numpy as np


D,G = map(int, input().split())
pc = [list(map(int, input().split())) for _ in range(D)]
p,c = [list(i) for i in zip(*pc)]

ans=sum(p)
for v in itertools.product([0,1],repeat=D):
    pdb.set_trace()
    sums = 0
    count = 0
    for i in range(D):
        sums += v[i] * ((i + 1) * p[i] * 100 + c[i])
        count += v[i] * p[i]
    if sums >= G:
        ans = min(count, ans)
    else:
        for j in range(D):
            if v[-(j + 1)] == 0:
                k = 1
                while k * (D - j) * 100 < (G - sums):
                    k += 1
                count += k
                if k < p[-(j + 1)]:
                    ans = min(count, ans)
                break
print(ans)

'''
D, G = map(int, input().split())
H = [list(map(int, input().split())) for _ in range(D)]
bonus = [x[0] for x in H]
PC = [[i*100] * j[0] for i, j in enumerate(H, 1)]
X = []
for i in PC:
    X += i
X_col = collections.Counter(X)

min_total = float('INF')
for binary in itertools.product([0, 1], repeat=len(X)):
    #pdb.set_trace()
    tmp = []
    for i, ok in enumerate(binary):
        if ok == 1:
            tmp.append(X[i])
    tmp_col = collections.Counter(tmp)
    #pdb.set_trace()
    for i, key in enumerate(X_col.keys()):
        if X_col[key] == tmp_col[key]:
            #pdb.set_trace()
            tmp.append(H[i][1])
    print(binary, tmp)

    if sum(tmp) >= G and sum(binary) < min_total:
        min_total = sum(binary)
print(min_total)
'''


