import pdb
import itertools as iter

n, m = map(int, input().split())

'''
# 思いついたからやった方法
l_min = 0
r_max = float('INF')
for _ in range(m):
    l, r = map(int, input().split())
    if l > l_min:
        l_min = l
    if r < r_max:
        r_max = r

if r_max - l_min + 1 > 0:
    print(r_max - l_min + 1)
else:
    print(0)
'''

# imos法
imos = [0] * (10**5+5)
for _ in range(m):
    l, r = map(int, input().split())
    imos[l] += 1
    imos[r+1] -= 1
imos_acc = list(iter.accumulate(imos))
num = [x for x in imos_acc if x == m]
print(len(num))


