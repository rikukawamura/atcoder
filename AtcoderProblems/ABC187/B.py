import pdb
import itertools

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

count = 0
for i in range(n):
    for j in range(i+1, n):
        #pdb.set_trace()
        slope = (xy[i][1]-xy[j][1])/(xy[i][0]-xy[j][0])
        if slope >= -1 and slope <= 1:
            count+=1
print(count)