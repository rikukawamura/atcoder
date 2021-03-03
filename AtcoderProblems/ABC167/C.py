import pdb
import itertools
import numpy as np

#　行列計算的なことをしたいときは，numpyが便利
n, m, x = map(int, input().split())
ca = [list(map(int, input().split())) for _ in range(n)]

min_money = float('INF')
flag = False
for i in range(1, n+1):
    # 全ての参考書の組み合わせを総当たり
    for j in list(itertools.combinations(ca, i)):
        j = np.array(j)
        sum_j = np.sum(j, axis=0)
        if sum_j[0] <= min_money and all([i >= x for i in sum_j[1:]]):
            min_money = sum_j[0]
            flag = True
if flag:
    print(min_money)
else:
    print(-1)


