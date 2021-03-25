import pdb
import collections

k = int(input())
s = list(input())
t = list(input())
card = []
for i in range(1, 10):
    card.append([i]*k)
cards = collections.Counter(''.join(card))


s = list(map(int, ' '.join(s[:-1]).split()))
t = list(map(int, ' '.join(t[:-1]).split()))
temoti = collections.Counter(s+t)

pdb.set_trace()
