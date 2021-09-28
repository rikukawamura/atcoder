def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
import queue

X, Y = int_sp()
dp = [[0]*(X+1) for i in range(Y+1)]
q = queue.Queue()
q.put((0, 0 ,1)) # スタート地点をenqueue
mod = 10**9+7
while (not q.empty()):
    #pdb.set_trace()
    x, y, cnt = q.get()
    dp[y][x] += cnt
    if 0 <= x+1 <= X and 0 <= y+2 <= Y:
        q.put((x+1, y+2, dp[y][x]))
    if 0 <= x+2 <= X and 0 <= y+1 <= Y:
        q.put((x+2, y+1, dp[y][x]))
    #dp[i] = (dp[i-1]%mod) + (dp[i-2]%mod) # 一段前と二段前の段数のたどり着き方を足す．
print(dp[Y][X]%mod)