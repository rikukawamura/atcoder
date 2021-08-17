def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

import pdb

N, Q = int_sp()
A = li_int_sp()
A_dif = []
ans = 0
for i in range(1, N):
    A_dif.append(A[i]-A[i-1])
    ans += abs(A[i]-A[i-1])
pdb.set_trace()
for q in range(Q):
    L, R, V = int_sp()
    if L >= 2: # L==1の場合はAが1〜変動するため，不便さの変化がない．
        ans -= abs(A_dif[L-2])
        A_dif[L-2] += V
        ans += abs(A_dif[L-2])
    if R <= N-1: # R==N-1の時も，不便さの変化がない．
        ans -= abs(A_dif[R-1])
        A_dif[R-1] -= V
        ans += abs(A_dif[R-1])
    print(ans)


