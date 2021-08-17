def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

import pdb
from math import gcd

N, start = int_sp()
X = li_int_sp()
X = sorted(X+[start])

#各地点の差分
dif = []
for i in range(N):
    dif.append(X[i+1]-X[i])

# 各地点の値の最大公約数
gcds = dif[0]
for i in dif[1:]:
    gcds = gcd(gcds, i)
print(gcds)

# 移動回数を求める．
'''
total = 0
for i in dif:
    total += i//gcds
print(total)
'''

