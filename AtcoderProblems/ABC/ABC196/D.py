import sys
import pdb

sys.setrecursionlimit(10**6)
def dfs(i,j,a,b):
    pdb.set_trace()
    global res
    if a<0 or b<0:  # 畳がa枚以下やb枚以下になれば失敗
        return
    if j == W:      # 右端に来たら次の行へ
        j = 0
        i += 1
    if i == H:      # iがhになれば成功(条件にあう畳の敷き詰め方)
        res += 1
        return
    if used[i][j] == 1: # 調べるマスに畳があれば次のマスに
        return dfs(i,j+1,a,b)

    used[i][j] = 1
    dfs(i,j+1,a,b-1)    # 半畳 使う場合
    if j+1 < W and used[i][j+1] == 0:    #横に1畳置く場合
        used[i][j+1] = 1
        dfs(i,j+1,a-1,b)
        used[i][j+1] = 0

    if i+1 < H and used[i+1][j] == 0:   #縦に1畳置く場合
        used[i+1][j] = 1
        dfs(i,j+1,a-1,b)
        used[i+1][j] = 0

    used[i][j] = 0  # 元に戻す
    return res



H, W, a, b =map(int,input().split())
used = [[0]*W for _ in range(H)]
res = 0

# 畳の左上を初期値として，全探索
print(dfs(0, 0, a, b))