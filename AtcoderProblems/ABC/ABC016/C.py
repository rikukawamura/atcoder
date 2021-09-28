import sys
import queue
import pdb


input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, M = map(int,input().split())
edges= [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    edges[A-1].append(B-1)
    edges[B-1].append(A-1)

friends = [0]*N # 人iの友達の友達が何人いるかを格納
for i in range(N):
    visited = [False]*N
    tmp = [0]*N
    q = queue.Queue()
    q.put((i, 0)) # スタート地点(ノード, 前のノード）

    while (not q.empty()):
        node, cnt = q.get()
        if visited[node] == True: # 訪問済みの場合は無視する
            continue
        else:
            visited[node] = True
            tmp[node] = cnt
            for nxt in edges[node]:
                q.put((nxt, cnt+1))

    cnt = 0
    for j in tmp:
        if j == 2:
            cnt += 1
    friends[i] = cnt

for i in friends:
    print(i)