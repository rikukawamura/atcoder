def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

N = int(input())
edge = [[] for _ in range(N)]
color = [[False]*N for _ in range(N)]
for _ in range(N-1):
    a, b = int_sp()
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

