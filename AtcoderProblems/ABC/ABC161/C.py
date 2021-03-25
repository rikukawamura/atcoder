import pdb

n, k = map(int, input().split())

amari = n % k
output = abs(amari - k)

print(min(amari, output, n))