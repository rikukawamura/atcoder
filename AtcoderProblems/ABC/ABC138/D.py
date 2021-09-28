import pdb
import sys
import queue

def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

sys.setrecursionlimit(10**7)

N, Q = int_sp()
edges= [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

cnt = [0]*N
for q in range(Q):
    p, x = int_sp()
    cnt[p-1] += x

visited = [False]*N
output = [-1]*N
q = queue.Queue()
q.put((0, 0)) # スタート地点(ノード, ノード1の初期値）
tmp = 0
while (not q.empty()):
    node, val = q.get()
    if visited[node] == True: # 訪問済みの場合は無視する
        continue
    else:
        visited[node] = True # 訪問フラグを立てて，現在地の上下方向に移動可能ならばスタック
        output[node] = val + cnt[node]
        for nxt in edges[node]:
            q.put((nxt, output[node]))

print(*output)