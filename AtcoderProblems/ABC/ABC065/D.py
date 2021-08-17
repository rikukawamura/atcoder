def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
import heapq

N = int(input()) # ノード数

adj = []
for i in range(N):
    x, y = li_int_sp()
    adj.append([x, y, i])
visited = [0] * (N)
q = [[0]+adj[0]]    # (cost, v)
heapq.heapify(q)
ans = 0
while len(q):
    #pdb.set_trace()
    cost, x, y, v = heapq.heappop(q)
    if visited[v]:
        continue

    # そのノードと繋げる
    visited[v] = 1
    ans += cost

    # 新たに繋げたノードから行けるところをエンキュー
    for nxt_x, nxt_y, i in adj:
        heapq.heappush(q, (min(abs(x-nxt_x), abs(y-nxt_y)), nxt_x, nxt_y, i))
        i+=1
print(ans)