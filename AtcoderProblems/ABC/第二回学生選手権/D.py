import pdb
import itertools

N, P = map(int, input().split())
amari = 10**9+7

count = 0
for i in list(itertools.product(range(1, P), repeat=N)):
    #print(i)
    i_acc = list(itertools.accumulate(i))
    if all([True if x % P != 0 else False for x in i_acc]):
        count += 1
print(count % amari)