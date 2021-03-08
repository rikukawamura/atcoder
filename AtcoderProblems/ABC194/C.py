import pdb
import itertools

n = int(input())
a = list(map(int, (input().split())))
a_acc = list(itertools.accumulate(a))
a_2 = [x**2 for x in a]

comb = []
for i in range(0, n):
    #pdb.set_trace()
    comb.append(a[i] * (a_acc[-1]-a_acc[i]))


print(((n-1) * sum(a_2)) - 2 *sum(comb))