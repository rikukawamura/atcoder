import pdb
import math

total = []
n = int(input())
for i in range(2, int(math.sqrt(n))+1):
    j = 2
    while i**j <= n:
        total.append(i**j)
        j+=1
total = set(total)
pdb.set_trace()
print(n-len(total))
