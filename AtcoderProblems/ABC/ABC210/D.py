def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

H, W, C = int_sp()
A = [li_int_sp() for _ in range(H)]

min_val = float('INF')
for sy in range(H):
    for sx in range(W):
        for gy in range(sy, H):
            for gx in range(sx, W):
                if sy==gy and sx==gx:
                    continue
                if C*(abs(sy-gy)+abs(sx-gx)) >= min_val:
                    break
                cost = (A[sy][sx]+A[gy][gx])+C*(abs(sy-gy)+abs(sx-gx))
                min_val = min(min_val, cost)
print(min_val)