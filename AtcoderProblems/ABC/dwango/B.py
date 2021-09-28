def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from collections import defaultdict
S = input()

def syakutori():
    r, ans, max_val = 0, defaultdict(int), 0
    for l in range(N):
        while True:
            #pdb.set_trace()
            if r >= N: # r >= Nになるとlをインクリメント
                break
            if ans[A[r]] == 0:
                ans[A[r]] += 1
            else:
                break
            r += 1
        max_val = max(max_val, abs(r-l))
        if l == r:
            r += 1
        else:
            ans[A[l]] -= 1
            if ans[A[l]] == 0:
                del ans[A[l]]
    return max_val

ans = print(syakutori())