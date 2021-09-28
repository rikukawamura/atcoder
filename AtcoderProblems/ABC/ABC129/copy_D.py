def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from collections import defaultdict

H, W = int_sp()
maze = []
for _ in range(H):
    S = list(input())
    maze.append(S)
retu = list(map(list, (zip(*maze))))



gyou = [[] for i in range(H)]
ind = 0
for i in range(H):
    ind += 1
    for j in range(W):
        if maze[i][j] == '#':
            gyou[i].append('#')
            ind += 1
        else:
            gyou[i].append(ind)

retu2 = [[] for i in range(W)]
for i in range(W):
    ind += 1
    for j in range(H):
        if retu[i][j] == '#':
            retu2[i].append('#')
            ind += 1
        else:
            retu2[i].append(ind)


cnt = defaultdict(int)
for i in gyou:
    for j in i:
        cnt[j]+=1

for i in retu2:
    for j in i:
        cnt[j]+=1

max_val = 0
for i in range(H):
    #pdb.set_trace()
    for j in range(W):
        if maze[i][j] != '#':
            tmp = cnt[gyou[i][j]] + cnt[retu2[j][i]] - 1
            max_val = max(max_val, tmp)
print(max_val)