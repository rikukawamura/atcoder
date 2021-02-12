import pdb


n, x = map(int, input().split())
a = list(map(int, input().split()))
b = [c for c in a if c != x]
b = list(map(str, b))

print(' '.join(b))
