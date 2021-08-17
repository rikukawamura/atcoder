def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from itertools import accumulate
import numpy as np

N = int(input())
roop = 10
papers = np.array([[0]*(roop) for _ in range(roop)])

xy = []
for _ in range(N):
    lx, ly, rx, ry = int_sp()
    xy.append([lx,ly,rx,ry])

for lx, ly, rx, ry in xy:
    tmp = np.array([[0] * (roop) for _ in range(roop)])
    yoko = rx-lx
    tate = ry-ly
    tmp[ly][lx] = 1
    tmp[ry][rx] = 1
    tmp[ly][lx+yoko] = -1
    tmp[ry][rx-yoko] = -1

    #pdb.set_trace()
    for i in range(roop):
        tmp[i] = list(accumulate(tmp[i]))
    #pdb.set_trace()
    tmp = list(map(list, (zip(*tmp))))
    for i in range(roop):
        tmp[i] = list(accumulate(tmp[i]))
    papers += tmp
pdb.set_trace()

for i in range(1, N+1):
    print(np.sum(papers == i))