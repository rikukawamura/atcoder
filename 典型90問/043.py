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
deq.append((sy, sx, -1, -1)) # (スタート地点(y, x),方向転換回数-1(最初動いた時0にするため）, costをpush
change_direct[sy][sx] = -1
while deq:
    #pdb.set_trace()
    y, x, dire, cost = deq.popleft()
    for dx, dy, dire2 in dxdy:
        if (0 <= x + dx < W) and (0 <= y + dy < H) and maze[y + dy][x + dx] != '#':
            # 方向転換するのなら，コスト＋1
            if dire != dire2:
                if change_direct[y+dy][x+dx] < cost + 1:
                    continue
                change_direct[y + dy][x + dx] = cost + 1
                deq.append((y+dy, x+dx, dire2, cost+1))
            # 方向転換しないなら，コストはそのまま
            else:
                if change_direct[y+dy][x+dx] < cost:
                    continue
                change_direct[y + dy][x + dx] = cost
                deq.appendleft((y+dy, x+dx, dire2, cost))
print(change_direct[gy][gx])