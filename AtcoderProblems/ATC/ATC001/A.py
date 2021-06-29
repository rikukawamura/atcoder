import sys
import pdb

# 再帰上限解放
sys.setrecursionlimit(10**6)
def dfs(y,x):
    # 範囲外や壁，及び訪れたことがある場合は探索を打ち切る
    if y<0 or H<=y or x<0 or W<=x or graph[y][x]== "#" or visited[y][x]:
        return
    visited[y][x]=1 # 訪問の記録をつける
    for k in range(4):
        dfs(y+dy[k], x+dx[k]) # 現在地の上下左右を探索

H, W=map(int, input().split())
graph=[list(input()) for _ in range(H)]

#訪問したかを記録しておく(0:訪問未, 1:訪問済)
visited=[[0] * W for _ in range(H)]

# 現在地の「右，下，左，上」の順に探索
dx=[0,1,0,-1]
dy=[1,0,-1,0]

#スタートとゴールの位置を記録
for i in range(H):
    for j in range(W):
        if graph[i][j] == "s":
            sy,sx=i,j
        elif graph[i][j] == "g":
            gy,gx=i,j

# スタート地点を初期値として，全探索
dfs(sy,sx)
#pdb.set_trace()
# ゴール地点を訪問(visit[gx][gy] == 1)していたらYesを出力
print("Yes") if visited[gy][gx] else print("No")