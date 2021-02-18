import sys
import pdb
import pprint
import copy


sys.setrecursionlimit(1000000)
def dfs(x,y):
    if x<0 or 10<=x or y<0 or 10<=y or graph[x][y]=="x" or visit[x][y]:
        return 0
    visit[x][y]=1 #訪問の記録をつける
    for k in range(4):
        dfs(x+dx[k],y+dy[k])



steped=[list(input()) for i in range(10)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
sima = 0
# もともとの島の範囲を数える
for c in steped:
    for d in c:
        if d == 'o':
            sima += 1


for i in range(10):
    for j in range(10):
        # 海の一つをうめて陸地を探索
        if steped[i][j]=="x":
            total = 0
            visit = [[0 for i in range(10)] for j in range(10)]  # 訪問したかを記録しておく
            graph = copy.deepcopy(steped)
            graph[i][j]="o"
            flag = False
            # スタートの位置を決定(これは別にどこでもいい)
            for a in range(10):
                for b in range(10):
                    if graph[a][b] == "o":
                        sx, sy = a, b
                        flag = True
                        break
                if flag:
                    break
            dfs(sx,sy)
            # 陸地の数がsima + 1になっていれば島がひとつになったということ
            for k in visit:
                total += sum(k)
            if total == sima+1:
                print('YES')
                exit()
        else:
            continue
print('NO')