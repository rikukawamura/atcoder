import itertools
import pdb

'''
k, s = map(int, input().split())
x = list(range(k+1))
xyz = list(itertools.product(x, repeat=3))

count = 0
for y in xyz:
    if sum(y) == s:
        count += 1
print(count)
'''

k, s = map(int, input().split())
count = 0
for x in range(k + 1):
    for y in range(k + 1):
        z = s - x - y
        if 0 <= z <= k:
            count += 1
print(count)