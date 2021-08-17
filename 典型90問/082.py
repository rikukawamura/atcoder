def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

L, R = list(input().split())
mod = 10**9+7
len_L = len(L)
len_R = len(R)

total = 0
# 同じ長さ(ex. len = 2)である時に12~99なのか12~Rなのかで分岐．
while len_L <= len_R:
    if len_L != len_R:
        th = '9'*len_L
        total += (int(th)-int(L)+1)*(int(L)+int(th))//2 * len_L % mod
        L = int(th)+1
        len_L += 1
    else:
        total += (int(R) - int(L)+1) * (int(L) + int(R)) // 2 * len_L % mod
        len_L += 1

print(total%mod)