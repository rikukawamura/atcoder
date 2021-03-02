import pdb
import collections

n, m = map(int, input().split())
ps = [list(map(str, input().split())) for _ in range(m)]
ps = collections.Counter(ps)
pdb.set_trace()
# 各問題の正答を記録(1:AC済, 0:AC末済)
memo = [0]*n



