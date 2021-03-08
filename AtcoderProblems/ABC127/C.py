import pdb

n, m = map(int, input().split())

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


