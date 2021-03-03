import pdb

# https://qiita.com/NNNiNiNNN/items/d60aba2d052b3d4ff0a1を参考にした．
# c問題は，アルゴリズムというよりかは，初期値決めて全探索するのが多い気がする．
n, m = map(int, input().split())
h = list(map(int, input().split()))

# 全部とりあえず良い展望台
good = [True] * n

for _ in range(m):
  a, b = map(int, input().split())
  if h[a-1] >= h[b-1]:
    good[b-1] = False
  if h[a-1] <= h[b-1]:
    good[a-1] = False
print(sum(good))

