import pdb
import itertools

K = int(input())
count = 0
for i in range(1, K+1):
    for j in range(1, K+1):
        if i*j > K:
            break
        else:
            count += K // (i*j)
print(count)