import pdb
import queue

dxdy = ((-1,0), (1,0), (0,-1), (0,1)) # 現地点から上下左右移動するためのパラメータ

H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]

for h in range(H):
    for w in range(W):
        if C[h][w] == 's':
            sy, sx = h, w
        if C[h][w] == 'g':
            gy, gx = h, w

visited = [[[False]*3 for _ in range(W)] for _ in range(H)]
break_cnt = [[float('INF')]*W for _ in range(H)]


q = queue.Queue()
q.put((sy, sx, 0))

while not q.empty():
    #pdb.set_trace()
    y, x, d = q.get()
    if y == gy and x == gx:
        visited[y][x][d] = True
        break
    if visited[y][x][d]:
        continue
    visited[y][x][d] = True
    for dx, dy in dxdy:
        if (0 <= y + dy < H) and (0 <= x + dx < W) and not visited[y + dy][x + dx][d]:  # 範囲内に収まっているか
            if C[y + dy][x + dx] == '#' and d <= 1:  # 未訪問かつ通行可能か
                #pdb.set_trace()
                q.put((y + dy, x + dx, d + 1))  # 距離を+1してenqueue
            #elif visited[y + dy][x + dx] == 0 and C[y + dy][x + dx] == '#' and d > 1:  # 未訪問かつ通行可能か
                # pdb.set_trace()
            #    break_cnt[y + dy][x + dx] = -1
            elif (C[y + dy][x + dx] == '.' or C[y + dy][x + dx] == 'g'):
                q.put((y + dy, x + dx, d))  # 距離を+1してenqueue
pdb.set_trace()

if any(visited[gy][gx]):
    print('YES')
else:
    print('NO')

