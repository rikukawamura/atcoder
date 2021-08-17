import sys
import pdb
N, M = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]

# 初期化(無限値）．
dist = [[1 << 60] * N for i in range(N)]

# s==tの場合は0を格納．
for i in range(N):
  dist[i][i] = 0

# distにa->bの移動時間を格納．
for a, b, c in ABC:
  dist[a - 1][b - 1] = c

# ワーシャルフロイド法
answer = 0 # kを経由した時のi->jの最短経路を記録．
for k in range(N):
  for i in range(N):
    for j in range(N):
      dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) #直接(i->j)とk王国を経由(i->k->j)の最小値を格納．
      if dist[i][j] < 1 << 60: # d[i][j]がinfの場合はans+=0だから．
        answer += dist[i][j] # kを経由した時のi->jの最短距離を追加

print(answer)
