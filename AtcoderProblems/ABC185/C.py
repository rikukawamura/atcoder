import pdb
import itertools
import math

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

l = int(input())
vars = comb(l-1, 11)
print(vars)