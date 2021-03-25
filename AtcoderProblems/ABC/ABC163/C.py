import collections
import pdb

n = int(input())
a = collections.Counter(list(map(int, input().split())))
#pdb.set_trace()

for i in range(1, n+1):
    print(a[i])

