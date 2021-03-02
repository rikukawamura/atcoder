'''
TLEになる．https://qiita.com/u2dayo/items/204b73fdb98fa5e4a543を参考にするとうまくいく．
'''

import itertools
import operator
import functools
import pdb

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

N = int(input())
x = prime_factorize(N)
pairs = []
for i in range(1,len(x)+1):
    for j in itertools.combinations(x, i):
        pairs.append(j)

output = []
for j in set(pairs):
    output.append(functools.reduce(operator.mul, j))
output.append(1)

for i in sorted(output):
    print(i)
