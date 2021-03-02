import pdb
import collections


n, a, b = map(int, input().split())
ab = ['b']*a + ['r']*b
pairs = collections.Counter(ab)
c = n // len(ab)
bleus = pairs['b'] * c

amari = n % len(ab)
amari = ab[:amari]
bleus += collections.Counter(amari)['b']
print(bleus)