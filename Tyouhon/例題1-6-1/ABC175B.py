import math
import itertools
import pdb

n = int(input())
l = list(map(int, input().split()))

count = 0
for i in itertools.combinations(l, 3):
    if (i[0] != i[1] and i[0] != i[2] and i[1] != i[2]) and (i[0]+i[1]>i[2] and i[0]+i[2]>i[1] and i[1]+i[2]>i[0]):
        count += 1
print(count)