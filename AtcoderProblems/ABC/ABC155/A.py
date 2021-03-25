import pdb
import collections

abc = list(map(int, input().split()))
abc_col = collections.Counter(abc)

if len(abc_col) == 1 or len(abc_col) == 3:
    print('No')
else:
    print('Yes')
