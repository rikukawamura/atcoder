from heapq import heappush, heappop
import pdb
INF = 10 ** 9
def dijkstra(s, n): # (始点, ノード数)
    dist = [INF] * n
    hq = [(0, s)] # (distance, node)
    dist[s] = 0
    seen = [False] * n # ノードが確定済みかどうか
    while hq:
        #pdb.set_trace()
        v = heappop(hq)[1] # ノードを pop する
        seen[v] = True
        for to, cost in adj[v]: # ノード v に隣接しているノードに対して
            #pdb.set_trace()
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist

# ノード数, エッジ数, 始点ノード
N, M = map(int, input().split())
# adj[s]: ノード s に隣接する(ノード, 重み)をリストで持つ
adj = [[] for _ in range(N)]
for i in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    adj[A].append((B, C))
    adj[B].append((A, C)) # 無向グラフの場合はコメントアウト

#pdb.set_trace()
output1 = dijkstra(0, N)
output2 = dijkstra(N-1, N)

for i in range(N):
    print(output1[i]+output2[i])
