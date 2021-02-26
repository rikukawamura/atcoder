import string
import collections
import pdb

a = list(input())
b = list(string.ascii_lowercase)
col = collections.Counter(a)
#pdb.set_trace()

c = a.copy()
if len(a)==1 and a[0]=='a':
    print(-1)
    exit()
elif len(col)==1 and 'a' in dict(col).keys():
    print(''.join(a[:-1]))
    exit()
elif c[-1] == 'a':
    print(''.join(a[:-1]))
    exit()
else:
    c[-1] = b[0]

print(''.join(c))
