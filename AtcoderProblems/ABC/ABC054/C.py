def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

import pdb
from itertools import permutations

N, M = int_sp()
edges = [[False]*N for _ in range(N)] # 頂点(i, j)が繋がっているかを格納．
for _ in range(M):
    a, b = int_sp()
    edges[a-1][b-1] = True
    edges[b-1][a-1] = True

cnt = 0
for i in permutations(range(N)): # 探索ノード順を生成
    if i[0] != 0: # 一番最初のノードが0出なければ無視
        continue
    for j in range(N): # リストの最後まで回すようにするが，
        if j == N-1: # N-1まで回ればone-stroke-pathになっている．
            cnt += 1
            break
        if edges[i[j]][i[j+1]] == False: # ここでi[N-2][N-1]（iの最後まで繋がっているかを判定している)
            break
print(cnt)



