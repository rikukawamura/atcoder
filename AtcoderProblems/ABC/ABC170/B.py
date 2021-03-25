import pdb
import itertools

x, y = map(int, input().split())
foot = [2,4]
comb = list(itertools.combinations_with_replacement(foot, x))
#pdb.set_trace()

for i in comb:
    if y == sum(i):
        print('Yes')
        exit()

print('No')
