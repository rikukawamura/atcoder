def int_split():
    return map(int, input().split())

def list_int_split():
    return list(map(int, input().split()))

import pdb
import itertools


A = list_int_split()

for a, b, c in list(itertools.permutations(A)):
    if (c - b) == (b - a):
        print('Yes')
        exit()

print('No')
