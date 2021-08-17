import pdb

INF = 10 ** 12 # cの値に気をつけて初期値を決める
def bellmanford(r, v): # (始点, ノード数)
    dist = [-INF] * v # 初期値は-無限大
    dist[r] = 0 # 始点のは0に初期化
    neg_circle = [False]*N # 負閉路の場所を記録
    for i in range(v): # 何周目かをカウント
        change = False # i周目にdistが変更されたかのflag
        for s, t, d in edges:
            s = s-1
            t = t-1
            if dist[s] == -INF:
                continue
            if dist[s]+d > dist[t]:
                if i+1 == v:
                    neg_circle[t] = True
                dist[t] = dist[s]+d
                change = True
            else:
                continue
        if not change:
            break
    return dist, neg_circle


# ノード数, エッジ数, 始点ノード
N, M = map(int, input().split())
edges = []*N
for i in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
output, neg_circle = bellmanford(0, N)
if neg_circle[N-1] == True:
    print('inf')
else:
    print(output[N-1])

