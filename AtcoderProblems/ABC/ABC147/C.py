import pdb
import copy

syougen = []
N = int(input())
max_val = -float('INF')
for _ in range(N):
    tmp = []
    A = int(input())
    for _ in range(A):
        tmp.append(list(map(int, input().split())))
    syougen.append(tmp)

hypo = []
for bit in range(1 << N):
    tmp = []
    for i in range(N):
        if 1 & (bit >> i):
            tmp.append(1)
        else:
            tmp.append(0)
    hypo.append(tmp)


for bit in range(1 << N):
    true_syougen = []
    for i in range(N):
        if 1 & (bit >> i):
            true_syougen.append(syougen[i])

    for i in true_syougen:
        for j in i:
            if j[1] != hypo[bit][j[1]]:




pdb.set_trace()