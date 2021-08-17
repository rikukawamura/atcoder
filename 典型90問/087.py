# pypyで提出しないとTLEになる．
import sys
import pdb
N, P, K = map(int, input().split())
dist = [list(map(int, input().split())) for _ in range(N)]

'''
# 初期化(無限値）．
dist = [[1 << 60] * N for i in range(N)]

# s==tの場合は0を格納．
for i in range(N):
  dist[i][i] = 0

# distにa->bの移動時間を格納．
for i, X in enumerate(adj):
    for x in X:
        dist[i][x-1] = c
pdb.set_trace()
'''

pdb.set_trace()
# ワーシャルフロイド法
answer = 0 # kを経由した時のi->jの最短経路を記録．
for k in range(N):
  for i in range(N):
    for j in range(N):
      dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) #直接(i->j)とk王国を経由(i->k->j)の最小値を格納．
      if dist[i][j] < 1 << 60: # d[i][j]がinfの場合はans+=0だから．
        answer += dist[i][j] # kを経由した時のi->jの最短距離を追加
pdb.set_trace()
print(answer)