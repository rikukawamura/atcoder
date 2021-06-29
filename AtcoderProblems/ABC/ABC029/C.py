import pdb
import itertools

N = int(input())
for iter in list(itertools.product(['a', 'b', 'c'], repeat=N)):
    print(''.join(iter))
