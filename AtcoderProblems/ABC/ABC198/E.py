def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
import sys

sys.setrecursionlimit(10**7)
N = int(input())
C = li_int_sp()
edge = [[]*N for _ in range(N)]
for _ in range(N-1):
    A, B = int_sp()
    edge[A-1].append(B-1)
    edge[B-1].append(A-1)

def dfs(v):
    pdb.set_trace()
    origin_temp = temp[v]
    origin_color = color[C[v]]
    if temp[v]: return  # 同じ頂点を2度以上調べないためのreturn
    temp[v]=True
    if color[C[v]] == False:
        good.append(v+1)
    color[C[v]] = True
    for vv in edge[v]: dfs(vv)
    # vからデタッチする時は，tempとcolorをvを訪れる前の状態に戻す
    temp[v]= origin_temp
    color[C[v]] = origin_color

color = [False]*(10**5+10)
temp = [False]*N
good = []
dfs(0)
good.sort()
for i in good:
    print(i)
