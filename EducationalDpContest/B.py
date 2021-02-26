import pdb

n, k = map(int, input().split())
h = list(map(int, input().split()))

dp = [float('INF')] * 100000
dp[0]=0
for i in range(1, n):
    for j in range(max(0, i-k), i):
        dp[i] = min(dp[i], dp[j]+abs(h[i]-h[j]))
print(dp[n-1])