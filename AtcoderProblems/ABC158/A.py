import collections
import pdb

s = list(input())
s = collections.Counter(s)

if len(s)==1:
    print('No')
else:
    print('Yes')
