import pdb
from math import ceil

N, K = map(int, input().split())
A = list(map(int, input().split()))

print(1 + ceil((N-K)/(K-1)))