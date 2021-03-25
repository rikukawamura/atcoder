#import pdb
from math import sqrt
from itertools import combinations


n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

max_len = 0
for point in combinations(points, 2):
    x = sqrt((point[0][0] - point[1][0]) ** 2 + (point[0][1] - point[1][1]) ** 2)
    if x > max_len:
        max_len = x
print(max_len)

