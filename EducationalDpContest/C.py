import pdb


n = int(input())

# a,b,cを入力するためのリストを作っておく
a = [0] * (n + 1)
b = [0] * (n + 1)
c = [0] * (n + 1)

# DPの結果を入れるリストを作っておく
dp = [[0] * 3 for i in range(n + 1)]

# a,b,cを入力する
for i in range(1, n + 1):
    a[i], b[i], c[i] = map(int, input().split())

# i番目にa,b,cが選ばれた場合それぞれに対しての最大幸福度をもとめる
for i in range(1, n + 1):
    # i=1(1日目)はそのまま代入
    if i == 1:
        dp[i][0] = a[1]
        dp[i][1] = b[1]
        dp[i][2] = c[1]
    # 2日目移行は(i-1)日目に行っていないものから最大値を選択
    else:
        dp[i][0] = max(dp[i - 1][1] + a[i], dp[i - 1][2] + a[i])
        dp[i][1] = max(dp[i - 1][0] + b[i], dp[i - 1][2] + b[i])
        dp[i][2] = max(dp[i - 1][0] + c[i], dp[i - 1][1] + c[i])
pdb.set_trace()
# n日目にa,b,cそれぞれ選んだ場合の最大値を比較して出力
print(max(dp[n][0], dp[n][1], dp[n][2]))