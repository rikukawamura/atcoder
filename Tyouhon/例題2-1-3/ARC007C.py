import sys
import queue
import pdb


input = sys.stdin.readline
sys.setrecursionlimit(10**7)
dxdy = ((-1,0), (1,0), (0,-1), (0,1)) # 現地点から上下左右移動するためのパラメータ

R, C = map(int,input().split())
sy, sx = map(int,input().split())
gy, gx = map(int,input().split())
maze = []
visited = [[0]*C for _ in range(R)]

for r in range(R):
    s = input()
    maze.append(s) # 二次元リストにせず、文字列のリストのままでOK
q = queue.Queue()
q.put((sy-1,sx-1,0)) # スタート地点をenqueue

while (not q.empty()):
    y, x, d = q.get()
    #print(y, x, d)
    if x == gx-1 and y == gy-1: # ゴールにたどり着いたら終了
        ans = d
        break
    if visited[y][x] == 1: # 訪問済みの場合は無視する
        continue
    else:
        visited[y][x] = 1 # 訪問フラグを立てて，現在地の上下方向に移動可能ならばスタック
        for dx, dy in dxdy:
            if (0 <= x+dx < C) and (0 <= y+dy < R): # 範囲内に収まっているか
                if visited[y+dy][x+dx] == 0 and maze[y+dy][x+dx]=='.': # 未訪問かつ通行可能か
                    q.put((y+dy,x+dx,d+1)) # 距離を+1してenqueue
print(ans)