def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N = int(input())
A = li_int_sp()
dp = [0]*N
dp[1] = abs(A[0]-A[1])
for i in range(2, N):
    dp[i] = min(abs(A[i]-A[i-2])+dp[i-2], abs(A[i]-A[i-1])+dp[i-1])
print(dp[N-1])