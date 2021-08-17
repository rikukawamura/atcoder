def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

#
K = int(input())
mod = 10**9+7
if K % 9 != 0:
    print(0)
    exit()

#pdb.set_trace()
dp=[0]*(10**5)
dp[0] = 1
for i in range(1, K+1):
    B = min(i, 9)
    for j in range(1, B+1):
        dp[i] += dp[i-j]
print(dp[K]%mod)

