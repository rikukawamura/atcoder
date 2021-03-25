import sys
import queue
import pdb


input = sys.stdin.readline
sys.setrecursionlimit(10**7)
dxdy = ((-1,0), (1,0), (0,-1), (0,1)) # 現地点から上下左右移動するためのパラメータ

H, W, N = map(int,input().split())
graph = [list(input().strip())for _ in range(H)]


# 各工場の座標を獲得
lattice = []
for i in range(H):
    for j in range(W):
        if graph[i][j] == 'S':
            lattice.append([0, i, j])
        if graph[i][j] in map(str, list(range(1, N+1))):
            lattice.append([int(graph[i][j]), i, j])
lattice = sorted(lattice)
#pdb.set_trace()

time = 0
for i in range(len(lattice)-1):
    visited = [[0] * W for _ in range(H)]
    q = queue.Queue()
    q.put((lattice[i][1], lattice[i][2], 0))  # スタート地点をenqueue
    while (not q.empty()):
        y, x, d = q.get()
        #print(y, x, d)
        if y == lattice[i+1][1] and x == lattice[i+1][2]:  # ゴールにたどり着いたら終了
            time += d
            break
        if visited[y][x] == 1:  # 訪問済みの場合は無視する
            continue
        else:
            visited[y][x] = 1  # 訪問フラグを立てて，現在地の上下方向に移動可能ならばスタック
            for dx, dy in dxdy:
                if (0 <= x + dx < W) and (0 <= y + dy < H):  # 範囲内に収まっているか
                    if visited[y + dy][x + dx] == 0 and graph[y + dy][x + dx] != 'X':  # 未訪問かつ通行可能か
                        q.put((y + dy, x + dx, d + 1))  # 距離を+1してenqueue
print(time)