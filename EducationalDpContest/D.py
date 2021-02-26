import pdb


N, W = map(int, input().split())

w = [0] * (N + 1)
v = [0] * (N + 1)

for i in range(1, N + 1):
    w[i], v[i] = map(int, input().split())

# DP=i番目までの品物を重さがj以下になるように選んだ時の最大値
dp = [[0] * (W + 1) for i in range(N + 1)]


for i in range(1, N + 1):
    for j in range(1, W + 1):
        # i番目の品物を入れても重さがj以下なら
        if (j - w[i]) >= 0:
            dp[i][j] = max(dp[i - 1][j - w[i]] + v[i], dp[i - 1][j])
        # 重さがjを超えるなら
        else:
            dp[i][j] = dp[i - 1][j]

# 出力はN番目まで選んだ時の重さWの最大値
ans = dp[N][W]
print(ans)

