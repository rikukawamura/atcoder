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
sy, sx = int_sp()
gy, gx = int_sp()
sy -= 1
sx -= 1
gy -= 1
gx -= 1
maze = [input() for _ in range(H)]
warp_cnt = [[float('INF')] * W for _ in range(H)] # 初期値は無限大
deq = deque()
deq.append((sy, sx)) # スタート地点をpush
warp_cnt[sy][sx] = 0 # スタート地点のワープ回数は0
while len(deq) != 0:
    y, x = deq.popleft()
    if y == gy and x == gx:
        break
    # 01-BFSのコスト0の処理
    for dx, dy in dxdy:
        if (0 <= x + dx < W) and (0 <= y + dy < H) and maze[y+dy][x+dx]!='#':
            if warp_cnt[y + dy][x + dx] > warp_cnt[y][x]: # 遷移先の最短経路が遷移元よりも大きければ，上記の条件では遷移先の最短経路 = 遷移元の最短経路となるから更新する．
                warp_cnt[y + dy][x + dx] = warp_cnt[y][x]
                deq.appendleft((y+dy, x+dx))
    # 01-BFSのコスト1の処理
    for i in range(-2, 3):
        for j in range(-2, 3):
            if (0 <= x + j < W) and (0 <= y + i < H) and maze[y+i][x+j]!='#':
                if warp_cnt[y + i][x + j] > warp_cnt[y][x] + 1: # 遷移先の最短経路が遷移元+1より大きければ，遷移元+1で移動可能なので更新する．
                    warp_cnt[y + i][x + j] = warp_cnt[y][x] + 1
                    deq.append((y+i, x+j))

if warp_cnt[gy][gx] == float('INF'):
    print(-1)
else:
    print(int(warp_cnt[gy][gx]))