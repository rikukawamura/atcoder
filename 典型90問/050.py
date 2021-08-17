def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

N, L = int_sp()
dp = [0]*(N+1)
dp[0] = 1 #0段目には1を格納
mod = 10**9+7
for i in range(1, N+1): # 1~N段目を回す
    if 1 <= i < L: # 1~L-1段目までは1通りしか行き方がない(1->1->1..->i段目)
        dp[i] = dp[i-1]%mod
    else: # i-1段目の行き方+i-L段目の行き方
        dp[i] = (dp[i-1]%mod) + (dp[i-L]%mod)
print(dp[N]%mod)