def int_sp():
    return map(int, input().split())

def li_int_sp():
    return list(map(int, input().split()))

def dfs(y,x,cnt):
    if y == start_y and x == start_x and cnt >= 3:
        pos_root.append(cnt)
        return
    if y<0 or H<=y or x<0 or W<=x or masu[y][x]=="#" or visited[y][x]:
            return
    visited[y][x] += 1 #訪問の記録をつける
    for k in range(4):
        # 現在地の上下左右を探索
        dfs(y+dy[k],x+dx[k], cnt+1)

import sys
import pdb

sys.setrecursionlimit(10 ** 6)
H, W = int_sp()
masu = [list(input()) for _ in range(H)]
pos_root = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for start_y in range(H):
    for start_x in range(W):
        if masu[start_y][start_x] == '#':
            continue
        else:
            visited = [[0]*W for _ in range(H)]
            dfs(start_y, start_x, 0)

if pos_root == []:
    print(-1)
else:
    print(max(pos_root))



