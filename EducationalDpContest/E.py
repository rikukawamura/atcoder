import pdb
import numpy as np

N, W = map(int, input().split())
v_max = 10**5+1
w = [0] * (N + 1)
v = [0] * (N + 1)

for i in range(1, N + 1):
    w[i], v[i] = map(int, input().split())

dp = [[float('INF')] * (v_max) for i in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    for j in range(v_max):
        if (j - v[i]) >= 0:
            dp[i][j] = min(dp[i - 1][j - v[i]] + w[i], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

ans = 0
for i in range(v_max):
    if dp[N][i] <= W:
        ans = max(ans, i)
print(ans)