import pdb
import itertools
import math

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

total_dis = 0
count_dis = 0
for comb in list(itertools.permutations(xy, n)):
    for i in range(len(comb)-1):
        total_dis += math.sqrt((comb[i][0]-comb[i+1][0])**2 + (comb[i][1]-comb[i+1][1])**2)
    count_dis += 1
print(total_dis / count_dis)