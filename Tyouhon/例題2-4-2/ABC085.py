import pdb

N = int(input())
X = sorted(set([int(input()) for _ in range(N)]))
print(len(X))
