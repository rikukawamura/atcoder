def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))


def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from collections import defaultdict

N, K = int_sp()
A = li_int_sp()


r, ans = 0, 0
tmp = defaultdict(int)
for l in range(N): # lを固定してrを+1していく．
    pdb.set_trace()
    while True:
        if len(tmp) > K: # [l, r]にK種類を超過していればbreak.
            break
        if r >= N: # rが範囲外になったら，現在の[l,r(最後まで）]は，OKだから+1してやる．
            r += 1
            break
        tmp[A[r]] += 1
        r += 1
    ans = max(ans, r - l - 1)

    if l == r:
        r += 1
    else:
        tmp[A[l]] -= 1
        if tmp[A[l]] == 0:
            del tmp[A[l]]
print(ans)

