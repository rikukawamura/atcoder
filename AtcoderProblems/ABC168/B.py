import pdb

k = int(input())
s = list(input())
#pdb.set_trace()
if len(s) <= k:
    print(''.join(s))
else:
    print(''.join(s[:k])+'...')