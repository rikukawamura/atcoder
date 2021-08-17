def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

def dijkstra(s, n): # (始点, ノード数)
    dist = [INF] * n
    hq = [(0, s)] # (distance, node)
    dist[s] = 0
    seen = [False] * n # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1] # ノードを pop する
        seen[v] = True
        for to, cost in adj[v]: # ノード v に隣接しているノードに対して
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist
import pdb
from heapq import heappush, heappop
N = int(input())
S = li_int_sp()
T = li_int_sp()
INF = 10 ** 9

# ノード数, 始点ノード
v, r = N+1, 0
# adj[s]: ノード s に隣接する(ノード, 重み)をリストで持つ
adj = [[] for _ in range(v)]
for i, t in enumerate(T, 1):
    adj[0].append((i, t))

for i, s in enumerate(S, 1):
    if (i+1)%v == 0:
        adj[N].append((1, s))
    else:
        adj[i].append((i+1, s))

output = dijkstra(r, v)
#pdb.set_trace()

for i in output[1:]:
    print(i)



