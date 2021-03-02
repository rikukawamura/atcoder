import pdb
import itertools


n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

count = 0
for i in itertools.permutations(xy, 3):
    if (i[2][1]-i[0][1]) * (i[1][0]-i[0][0]) == (i[1][1]-i[0][1]) * (i[2][0]-i[0][0]):
        print('Yes')
        exit()

print('No')