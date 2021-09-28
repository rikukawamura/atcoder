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
    r, ans = 0, 0 # ansは含まれる要素を管理
    for l in range(len(S)):
        while True:
            #pdb.set_trace()
            print(l, r)
            if r >= len(S): # r >= Nになるとlをインクリメント
                break
            if r-l < 4:
                r += 1
                continue
            elif r-l >= 4 and int(S[l:r])%2019 == 0:
                ans += 1
            r += 1
        if l == r:
            r += 1
    return ans

ans = print(syakutori())