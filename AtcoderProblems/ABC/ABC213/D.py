import sys
import pdb
from itertools import groupby

def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

# 再帰上限解放
sys.setrecursionlimit(10**6)
def dfs(node):
    # 範囲外や壁，及び訪れたことがある場合は探索を打ち切る
    if visited[node]:
        return
    visited[node]=1 # 訪問の記録をつける
    root.append(node + 1)
    for k in edges[node]:
        dfs(k)
        root.append(node + 1)

N = int(input())
edges = [[] for i in range(N)]
for _ in range(N-1):
    A, B = int_sp()
    edges[A-1].append(B-1)
    edges[B-1].append(A-1)
#訪問したかを記録しておく(0:訪問未, 1:訪問済)
#pdb.set_trace()
for i in range(len(edges)):
    edges[i] = sorted(edges[i])
visited = [0] * N

# スタート地点を初期値として，全探索
root = []
dfs(0)
x = groupby(root)
output = []
for i in x:
    output.append(i[0])
print(*output)