def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


# Falseならmidをngにセット，Trueならmidをokにセット
def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        pdb.set_trace()
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

def is_ok(x):
    ls = []
    for i in range(N):
        ls.append((x-H[i])//S[i]) # いつまでに割ればいいかの，秒数を計算．
    ls.sort() # 期限が近いものから先にわる
    for n in range(N):
        if (ls[n] < n):
            return False # 時間ぎれ
    return True

import pdb
from math import log
print(log(10**19)+(10**5)*2)
N = int(input())
H, S = [], []
for _ in range(N):
    h, s = int_sp()
    H.append(h)
    S.append(s)
print(meguru_bisect(0, 10**19))
