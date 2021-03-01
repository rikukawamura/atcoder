import itertools
import pdb

n = int(input())
total = 0
for i in range(n):
    a, b = map(int, input().split())
    total += ((b-a+1)/2) * (2*a + (b-a)*1)
print(int(total))