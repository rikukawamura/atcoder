def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import sys
from collections import deque
import pdb
import pprint
import numpy as np


input = sys.stdin.readline
sys.setrecursionlimit(10**7) # 再帰上限解放
dxdy = ((-1,0), (1,0), (0,-1), (0,1)) # 現地点から上下左右移動するためのパラメータ

H, W = map(int, input().split())
maze = [input() for _ in range(H)]
for i in range(H):
    for j in range(W):
        if maze[i][j]=='s':
            sy = i
            sx = j
        if maze[i][j] == 'g':
            gy = i
            gx = j
broken_block = np.array([[float('INF')] * W for _ in range(H)]) # 初期値は無限大
deq = deque()
deq.append((sy, sx))
# スタート地点のブロックは回数は0
broken_block[sy][sx] = 0
while deq:
    #pdb.set_trace()
    y, x = deq.popleft()
    #print(broken_block)
    for dx, dy in dxdy:
        if (0 <= x + dx < W) and (0 <= y + dy < H) and broken_block[y + dy][x + dx] == float('INF'):
            if maze[y+dy][x+dx]=='#':
                broken_block[y + dy][x + dx] = broken_block[y][x] + 1
                deq.append((y+dy, x+dx))
            else:
                broken_block[y + dy][x + dx] = broken_block[y][x]
                deq.appendleft((y+dy, x+dx))
print('YES') if broken_block[gy][gx] <= 2 else print('NO')