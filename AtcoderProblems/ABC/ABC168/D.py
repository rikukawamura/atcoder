import sys
import queue
import pdb


input = sys.stdin.readline
sys.setrecursionlimit(10**7)
dxdy = ((-1,0), (1,0), (0,-1), (0,1)) # 現地点から上下左右移動するためのパラメータ

N, M = map(int,input().split())
edges= [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    edges[A-1].append(B-1)
    edges[B-1].append(A-1)
visited = [False]*N
mezirusi = [-1]*N
q = queue.Queue()
q.put((0, -1)) # スタート地点(ノード, 前のノード）

while (not q.empty()):
    node, pre = q.get()
    if visited[node] == True: # 訪問済みの場合は無視する
        continue
    else:
        visited[node] = True # 訪問フラグを立てて，現在地の上下方向に移動可能ならばスタック
        mezirusi[node] = pre+1
        for nxt in edges[node]:
            q.put((nxt, node))

for i in mezirusi[1:]:
    if i == -1:
        print('No')
        exit()

print('Yes')
for i in mezirusi[1:]:
    print(i)