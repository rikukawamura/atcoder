def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
import queue

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    u, v, w = int_sp()
    # 連結している(ノード, 距離）を格納．
    graph[u-1].append([v-1, w])
    graph[v-1].append([u-1, w])

q = queue.Queue()
q.put((0,0)) # (スタート，白色）をセット．
visited = [False]*N
node = [0]*N # 各ノードの色を記録．
while (not q.empty()):
    now, grp = q.get()
    if visited[now] == True:
        continue
    visited[now] = True
    node[now] = grp
    for nxt, w in graph[now]: # 次の各ノードとノードの色を格納していく．
        if w%2==0: # 次のノードとの距離が偶数なら，今と同じ色を．
            q.put((nxt, grp))
        elif w%2==1: # 次のノードとの距離が奇数なら，今と違う色を(1と0を逆転させる）．
            q.put((nxt, 1-grp))

for i in node:
    print(i)
