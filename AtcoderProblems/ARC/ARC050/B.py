def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


# Falseならmidをngにセット，Trueならmidをokにセット
def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        #pdb.set_trace()
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

def is_ok(K):
    if K>R or K>B:
        return False
    if (R-K)//(x-1) + (B-K)//(y-1) >= K:
        return True
    return False


import pdb
from math import log
R, B = int_sp()
x, y = int_sp()
print(meguru_bisect(10**32, 0))