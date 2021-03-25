import sys
import pdb

sys.setrecursionlimit(10**6)
def dfs(x,y):
    # 範囲外や壁，及び訪れたことがある場合は探索を打ち切る
    if x<0 or h<=x or y<0 or w<=y or graph[x][y]=="#" or visit[x][y]:
        return 0
    visit[x][y]=1#訪問の記録をつける
    for k in range(4):
        # 現在地の上下左右を探索
        dfs(x+dx[k],y+dy[k])



h,w=map(int,input().split())
graph=[list(input())for i in range(h)]
visit=[[0 for i in range(w)] for j in range(h)]#訪問したかを記録しておく(0:訪問未, 1:訪問済)
# 現在地の「右，下，左，上」の順に探索
dx=[0,1,0,-1]
dy=[1,0,-1,0]
#スタートとゴールの位置を記録
for i in range(h):
    for j in range(w):
        if graph[i][j]=="s":
            sx,sy=i,j
        elif graph[i][j]=="g":
            gx,gy=i,j

# スタート地点を初期値として，全探索
dfs(sx,sy)

# ゴール地点を訪問(visit[gx][gy] == 1)していたらYesを出力
print("Yes") if visit[gx][gy] else print("No")