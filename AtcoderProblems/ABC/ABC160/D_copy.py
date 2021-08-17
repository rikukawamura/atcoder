def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

N, X, Y = int_sp()
edge = [[] for _ in range(N)]
for i in range(N-1):
    A, B = i, i+1
    edge[A].append(B)
    edge[B].append(A)
edge[X-1].append(Y-1)
edge[Y-1].append(X-1)

def dfs(v, time):
    pdb.set_trace()
    if temp[v]: return
    temp[v] = True
    vis_time[v] = time
    for nxt in edge[v]:
        dfs(nxt, time+1)


vis_time = [-1]*N
temp = [False]*N
dfs(0, 0)
pdb.set_trace()