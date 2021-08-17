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
    A, B = int_sp()
    graph[A-1].append(B-1)
    graph[B-1].append(A-1)
group = [[], []] # 二つのグループを用意．

q = queue.Queue()
q.put((0, 0)) # (今の頂点，group(0 or 1))．
visited = [False]*N # 訪れた頂点を記録．
while (not q.empty()):
    now, grp = q.get()
    if visited[now] == True:
        continue
    visited[now] = True
    group[grp].append(now+1)
    for i in graph[now]: # 今の頂点に連結している頂点をqにputする．
        q.put((i, 1-grp))

if len(group[0])>=len(group[1]): # 頂点数が多いグループから2//N個抽出．
    print(*group[0][:N//2])
else:
    print(*group[1][:N//2])
