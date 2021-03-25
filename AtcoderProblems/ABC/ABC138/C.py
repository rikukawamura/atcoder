import pdb
import itertools


n = int(input())
i = sorted(list(map(int, input().split())))
pdb.set_trace()
output = []
total_value = (i[0]+i[1]) / 2
for j in range(2, len(i)):
    total_value = (total_value + i[j]) / 2
print(total_value)
