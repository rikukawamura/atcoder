def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

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

import pdb
from math import ceil


N = int(input())
primes = prime_factorize(N)

if len(primes) == 1:
    print(0)
    exit()

len_primes = len(primes)
pdb.set_trace()
x = 1
while True:
    if pow(2, x) >= len_primes:
        print(x)
        exit()
    x += 1
