import pdb

n, k = map(int, input().split())
h = list(map(int, input().split()))

sort_h = sorted(h, reverse=True)
min_attack = sum(sort_h[k:])
print(min_attack)