def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)

import pdb
import math
N = int(input())
X, Y = int_sp()
INF = float('INF')
dp = [[[INF for _ in range(Y+1)] for _ in range(X+1)] for _ in range(N+1)]
pdb.set_trace()
AB = [li_int_sp() for _ in range(N)]
A, B = list(map(list, (zip(*AB))))
dp[0][0][0] = 0
for i in range(N):
    for j in range(X+1):
        for k in range(Y+1):
            if dp[i][j][k] == INF:
                continue
            # 弁当i個目を購入しない場合
            dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
            # 弁当i個目を購入する場合
            if j+A[i] >= X and k+B[i] <= Y:
                dp[i+1][X][k+B[i]] = min(dp[i+1][X][k+B[i]], dp[i][j][k]+1)
            elif j+A[i] <= X and k+B[i] >= Y:
                dp[i+1][j+A[i]][Y] = min(dp[i+1][j+A[i]][Y], dp[i][j][k]+1)
            elif j+A[i] >= X and k+B[i] >= Y:
                dp[i+1][X][Y] = min(dp[i+1][X][Y], dp[i][j][k]+1)
            else:
                dp[i+1][j+A[i]][k+B[i]] = min(dp[i+1][j+A[i]][k+B[i]], dp[i][j][k]+1)

pdb.set_trace()
if dp[N][X][Y] != INF:
    print(dp[N][X][Y])
else:
    print(-1)