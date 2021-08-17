def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import sys
from collections import deque
import pdb

input = sys.stdin.readline
sys.setrecursionlimit(10**7) # 再帰上限解放
dxdy = ((-1,0), (1,0), (0,-1), (0,1)) # 現地点から上下左右移動するためのパラメータ

H, W = map(int, input().split())
maze = [input() for _ in range(H)]
broken_block = [[float('INF')] * W for _ in range(H)] # 初期値は無限大
deq = deque()
deq.append((0, 0))
gy, gx = H-1, W-1 # ゴール地点
broken_block[0][0] = 0 # スタート地点のブロック破壊回数は0
while len(deq) != 0:
    y, x = deq.popleft()
    if y == gy and x == gx:
        break
    for dx, dy in dxdy:
        if (0 <= x + dx < W) and (0 <= y + dy < H) and maze[y+dy][x+dx]!='#':
            if broken_block[y+dy][x+dx] > broken_block[y][x]: # 遷移先の最短経路が遷移元よりも大きければ，上記の条件では遷移先の最短経路 = 遷移元の最短経路となるから更新する．
                broken_block[y + dy][x + dx] = broken_block[y][x]
                deq.appendleft((y+dy, x+dx))
    for i in range(-2, 3):
        for j in range(-2, 3):
            if (0 <= x + j < W) and (0 <= y + i < H) and abs(i)+abs(j) <= 3:
                if broken_block[y+i][x+j] > broken_block[y][x] + 1: # 遷移先の最短経路が遷移元+1より大きければ，遷移元+1で移動可能なので更新する．
                    broken_block[y+i][x+j] = broken_block[y][x] + 1
                    deq.append((y+i, x+j))

print(int(broken_block[gy][gx]))
