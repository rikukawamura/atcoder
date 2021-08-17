def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

N, M = int_sp()
A = [int(input()) for _ in range(M)] # 壊れている段数
dp = [0]*(N+1)
cheker = [False]*(N+1) # 壊れている段数をTrueにする．
for a in A:
    cheker[a] = True
dp[0] = 1
mod = 10**9+7
for i in range(1, N+1):
    if cheker[i]: # 壊れている段数はスキップ．=>　そこに辿り着く方法は0通り．
        continue
    if 1 == i:
        dp[i] = dp[i-1]%mod
    else:
        dp[i] = (dp[i-1]%mod) + (dp[i-2]%mod) # 一段前と二段前の段数のたどり着き方を足す．
print(dp[N]%mod)

