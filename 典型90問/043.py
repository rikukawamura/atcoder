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
dxdy = ((-1,0,0), (1,0,1), (0,-1,2), (0,1,3)) # 現地点から上下左右移動するためのパラメータ(3つ目のパラメータは方向を記録)

H, W = map(int, input().split())
sy, sx = int_sp()
gy, gx = int_sp()
sy, sx = sy-1, sx-1
gy, gx = gy-1, gx-1
maze = [input() for _ in range(H)]
change_direct = [[float('INF')] * W for _ in range(H)] # 初期値は無限大
deq = deque()
deq.append((sy, sx, -1)) # スタート地点と方向転換回数-1(最初動いた時0にするため）をpush
change_direct[sy][sx] = -1
while deq:
    #pdb.set_trace()
    y, x, dire = deq.popleft()
    for dx, dy, dire2 in dxdy:
        if (0 <= x + dx < W) and (0 <= y + dy < H) and change_direct[y + dy][x + dx] == float('INF') and maze[y + dy][x + dx] != '#':
            # 方向転換するのなら，コスト＋1
            if dire != dire2:
                change_direct[y + dy][x + dx] = change_direct[y][x] + 1
                deq.append((y+dy, x+dx, dire2))
            # 方向転換しないなら，コストはそのまま
            else:
                change_direct[y + dy][x + dx] = change_direct[y][x]
                deq.appendleft((y+dy, x+dx, dire2))
print(int(change_direct[gy][gx]))