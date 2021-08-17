def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
import sys
import queue
sys.setrecursionlimit(10**7)

N, K = int_sp()
grid = defaultdict(int)
for _ in range(M):
    A, B, C = int_sp()
    grid[A] = [B, C]

q = queue.Queue()
for s in range(N):
    for t in range(N):
        for k in range(N):
            q.put(s,0) # スタート地点をセット
            while (not q.empty()):



