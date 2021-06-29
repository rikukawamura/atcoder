import sys
import queue
import pdb

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
dxdy = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 現地点から上下左右移動するためのパラメータ

H, W = map(int, input().split())
visited = [[0] * W for _ in range(H)]

d = 0
max_val = 0
q = queue.Queue()
A = []
for h in range(H):
    A.append(list(input().strip()))
    for w in range(W):
        if A[h][w] == '#':
            q.put((h, w, d))
            


while not q.empty():
    y, x, count = q.get()
    if visited[y][x] == 1:
        continue
    else:
        visited[y][x] = 1
        A[y][x] = '#'
        for dx, dy in dxdy:
            if (0 <= x + dx < W) and (0 <= y + dy < H):  # 範囲内に収まっているか
                if visited[y + dy][x + dx] == 0 and A[y + dy][x + dx] == '.':  # 未訪問かつ通行可能か
                    A[y + dy][x + dx] = '#'
                    q.put((y + dy, x + dx, count + 1))

print(count)