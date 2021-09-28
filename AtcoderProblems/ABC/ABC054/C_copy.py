def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

import pdb
from itertools import permutations
from collections import defaultdict

N, M = int_sp()
edges = []
for _ in range(M):
    a, b = int_sp()
    edges.append((a-1, b-1))
    edges.append((b-1, a-1))

cnt = 0
for i in permutations(edges, N-1):
    pdb.set_trace()
    #if i == ((0, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1)):
        #pdb.set_trace()
    visited = [False]*N
    if i[0][0] != 0:
        continue
    visited[0] = True
    visited[i[0][1]] = True
    pre = i[0][1]
    for j in i[1:]:
        if j[0] == pre:
            visited[j[1]] = True
            pre = j[1]
        else:
            break
    #pdb.set_trace()
    if all(visited):
        cnt += 1
print(cnt)


