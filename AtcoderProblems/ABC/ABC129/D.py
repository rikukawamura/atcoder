def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from bisect import bisect_left
import sys

input = sys.stdin.readline
H, W = int_sp()
maze = []
for _ in range(H):
    S = list(input())
    maze.append(S)
retu = list(map(list, (zip(*maze))))

yoko = [[-1] for i in range(H)]
tate = [[-1] for i in range(W)]

for i in range(H):
    for j in range(W):
        if maze[i][j] == '#':
            yoko[i].append(j)
    yoko[i].append(W)

for i in range(W):
    for j in range(H):
        if retu[i][j] == '#':
            tate[i].append(j)
    tate[i].append(H)

max_val = 0
for i in range(H):
    for j in range(W):
        tmp=0
        #pdb.set_trace()
        if maze[i][j] == '#':
            continue
        x = bisect_left(yoko[i], j)
        y = bisect_left(tate[j], i)
        tmp += (yoko[i][x] - yoko[i][x-1]-1) + (tate[j][y] - tate[j][y-1] -1) -1
        max_val = max(max_val, tmp)
print(max_val)
