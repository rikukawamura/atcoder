import sys
import queue
import itertools
import pdb


input = sys.stdin.readline
sys.setrecursionlimit(10**7)
dxdy = ((-1,0), (1,0), (0,-1), (0,1)) # 現地点から上下左右移動するためのパラメータ

R, C = map(int, input().split())
maze = [input() for _ in range(R)]

road = []
for i in range(R):
    for j in range(C):
        if maze[i][j] == '.':
            road.append([i, j])


max_val = -float('INF')
for start in road:
    #pdb.set_trace()
    sy, sx = start
    visited = [[0] * C for _ in range(R)]
    q = queue.Queue()
    q.put((sy, sx, 0))  # スタート地点をenqueue
    while (not q.empty()):
        y, x, d = q.get()
        if visited[y][x] == 1:  # 訪問済みの場合は無視する
            continue
        else:
            visited[y][x] = 1  # 訪問フラグを立てて，現在地の上下方向に移動可能ならばスタック
            for dx, dy in dxdy:
                if (0 <= x + dx < C) and (0 <= y + dy < R):  # 範囲内に収まっているか
                    if visited[y + dy][x + dx] == 0 and maze[y + dy][x + dx] == '.':  # 未訪問かつ通行可能か
                        q.put((y + dy, x + dx, d + 1))  # 距離を+1してenqueue
        if d > max_val:
            max_val = d

print(max_val)