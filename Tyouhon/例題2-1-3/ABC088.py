import sys
import queue
import pdb


input = sys.stdin.readline
sys.setrecursionlimit(10**7)
dxdy = ((-1,0), (1,0), (0,-1), (0,1)) # 現地点から上下左右移動するためのパラメータ

H, W = map(int, input().split())
sy, sx = 0, 0
gy, gx = H-1, W-1
S = [input() for _ in range(H)]
visited = [[0] * W for _ in range(H)]

white_num = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            white_num += 1

q = queue.Queue()
q.put((sy,sx,0)) # スタート地点をenqueue

flag= False
while (not q.empty()):
    y, x, d = q.get()
    if x == gx and y == gy: # ゴールにたどり着いたら終了
        ans = d
        flag = True
        break
    if visited[y][x] == 1: # 訪問済みの場合は無視する
        continue
    else:
        visited[y][x] = 1 # 訪問フラグを立てて，現在地の上下方向に移動可能ならばスタック
        for dx, dy in dxdy:
            if (0 <= x + dx < W) and (0 <= y + dy < H): # 範囲内に収まっているか
                if visited[y+dy][x+dx] == 0 and S[y+dy][x+dx]=='.': # 未訪問かつ通行可能か
                    q.put((y+dy,x+dx,d+1)) # 距離を+1してenqueue

if flag:
    print(white_num-(ans+1))
else:
    print(-1)