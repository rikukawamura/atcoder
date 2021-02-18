#import pdb
from math import sqrt
from itertools import combinations


n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
'''
i = 0
max_len = 0
while i != len(zahyou):
    for j in zahyou[i+1:]:
        x = math.sqrt((zahyou[i][0] - j[0])**2 + (zahyou[i][1] - j[1])**2)
        if x > max_len:
            max_len = x
    i += 1

print(max_len)
'''

max_len = 0
for point in combinations(points, 2):
    #print(point)
    x = sqrt((point[0][0] - point[1][0]) ** 2 + (point[0][1] - point[1][1]) ** 2)
    if x > max_len:
        max_len = x
print(max_len)

