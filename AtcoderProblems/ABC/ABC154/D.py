import pdb
import itertools
import decimal


N, K = map(int, input().split())
P = list(map(int, input().split()))

exp = []
for p in P:
    exp.append(decimal.Decimal((1+p))/decimal.Decimal(2))

acc_exp = list(itertools.accumulate(exp))

max_val = acc_exp[K-1]
for i, j in enumerate(list(range(K, N))):
    tmp = acc_exp[j]-acc_exp[i]
    if tmp > max_val:
        max_val = tmp

print(max_val)