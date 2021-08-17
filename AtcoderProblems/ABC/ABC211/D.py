def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
import sys
import queue

input = sys.stdin.readline
sys.setrecursionlimit(10**7)
mod = 10**9+7
N, M = int_sp()
edges = [[] for _ in range(N)]
for _ in range(M):
    A, B = int_sp()
    A -= 1
    B -= 1
    edges[A].append(B)
    edges[B].append(A)

q = queue.Queue()
q.put((0, 0)) # (ノード，最短距離)
cnt = [0]*N
dist = [None]*N # そのノードに達することができる最短距離を格納
dist[0] = -1
cnt[0] = 1 # そのノードに最短距離で達することができる通り数
visited = [False]*N

while (not q.empty()):
    #pdb.set_trace()
    now, pre = q.get()
    if visited[now] == True:
        if dist[now] == dist[pre]+1:
            cnt[now] += cnt[pre]
    else:
        visited[now] = True
        dist[now] = dist[pre]+1
        cnt[now] = cnt[pre]
        for next in edges[now]:
            q.put((next, now)) # 距離を+1してenqueue
print(cnt[N-1]%mod)