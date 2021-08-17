def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

H, W = int_sp()
graph = [list(input()) for _ in range(H)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
visited = [[0] * W for _ in range(H)]

cnt = []
for i in range(H):
    for j in range(W):
        if graph[i][j] == '.':
            visited[i][j] = 1
            for y, x in zip(dy, dx):
                if i+y< 0 or H<=i+y or j+x<0 or W<=j+x or visited[i+y][j+x]:
                    continue
                if graph[i+y][j+x] == '.':
                    cnt.append([i+y, j+x])
print(len(cnt))
