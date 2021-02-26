n = int(input())
h = list(map(int, input().split()))
nor = [abs(h[i]-h[i-1]) for i in range(1, n)] #スキップなし
skip = [abs(h[i]-h[i+2]) for i in range(0, n-2)] #一個スキップ

dp = []
dp.append(0)
dp.append(nor[0])
del nor[0]
i=2
for x, y in zip(nor, skip):
    dp.append(min(dp[i-1]+x, dp[i-2]+y))
    i+=1
print(dp[-1])