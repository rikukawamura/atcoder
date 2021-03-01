import pdb
import collections


n, a, b = map(int, input().split())
ab = ['b']*a + ['r']*b
c = n // len(ab)
d = n % len(ab)
total_blue = a*c
amari = collections.Counter(ab[:d])
total_blue += amari['b']
print(total_blue)