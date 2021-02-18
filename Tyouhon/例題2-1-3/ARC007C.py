'''
import sys
import pdb
import pprint

sys.setrecursionlimit(1000000)
def dfs(x,y,i):
    if x<0 or c<=x or y<0 or r<=y or graph[x][y]=="#" or visit[x][y] != -1 :
        return 0
    #pdb.set_trace()
    visit[x][y]=i #訪問の記録をつける
    for k in range(4):
        dfs(x+dx[k],y+dy[k],i+1)



r,c=map(int,input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
graph=[list(input())for i in range(r)]
visit=[[-1 for i in range(c)]for j in range(r)]#訪問したかを記録しておく
#stepped = [[0 for i in range(c)]for j in range(r)]#訪問したかを記録しておく
dx=[0,1,0,-1]
dy=[1,0,-1,0]
dfs(sx-1,sy-1,0)
pprint.pprint(visit)
print(visit[gx][gy]-1)
'''

import sys
import queue
import pdb
input = sys.stdin.readline
sys.setrecursionlimit(int(1E+7))
dxdy = ((-1,0), (1,0), (0,-1), (0,1)) # タプルやリストで持っておくと便利
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
while(not q.empty()):
    y, x, d = q.get()
    if x == gx-1 and y == gy-1: # ゴールにたどり着いたら終了
        ans = d
        break
    if visited[y][x] == 1: # 訪問済みの場合は無視する
        continue
    else:
        visited[y][x] = 1 # 訪問フラグを立てる
        for dx, dy in dxdy:
            if (0<= x+dx < C) and (0<= y+dy < R): # 範囲内に収まっているか
                if visited[y+dy][x+dx] == 0 and maze[y+dy][x+dx]=='.': # 未訪問かつ通行可能か
                    q.put((y+dy,x+dx,d+1)) # 距離を+1してenqueue
print(ans)