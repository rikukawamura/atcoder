def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))


def dfs(s_y, s_x):
    if s_y<0 or H<=s_y or s_x<0 or W<=s_x or visited[s_y][s_x] or maps[s_y][s_x]==0:
        return
    visited[s_y][s_x] = 1
    for k in range(4):
        dfs(s_y+dy[k], s_x+dx[k])



import pdb
import sys


sys.setrecursionlimit(10**8)
H, W = int_sp()
Q = int(input())
maps = [[0]*W for _ in range(H)]
visited = [[0] * W for _ in range(H)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for _ in range(Q):
    #pdb.set_trace()
    q = li_int_sp()
    if q[0] == 1:
        maps[q[1]-1][q[2]-1] = 1
    else:
        start_y, start_x = q[1], q[2]
        goal_y, goal_x = q[3], q[4]
        dfs(start_y-1, start_x-1)
        if visited[goal_y-1][goal_x-1] == 1:
            print('Yes')
        else:
            print('No')
        visited = [[0]*W for _ in range(H)]
