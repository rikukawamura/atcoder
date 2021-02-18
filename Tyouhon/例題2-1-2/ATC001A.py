import sys
import pdb


sys.setrecursionlimit(1000000)
def dfs(x,y):
    #pdb.set_trace()
    if x<0 or h<=x or y<0 or w<=y or graph[x][y]=="#" or visit[x][y]:
        return 0
    visit[x][y]=1#訪問の記録をつける
    for k in range(4):
        dfs(x+dx[k],y+dy[k])



h,w=map(int,input().split())
graph=[list(input())for i in range(h)]
visit=[[0 for i in range(w)]for j in range(h)]#訪問したかを記録しておく
dx=[0,1,0,-1]
dy=[1,0,-1,0]
#スタートとゴールの位置を記録
for i in range(h):
    for j in range(w):
        if graph[i][j]=="s":
            sx,sy=i,j
        elif graph[i][j]=="g":
            gx,gy=i,j
dfs(sx,sy)
#pdb.set_trace()
print("Yes") if visit[gx][gy] else print("No")