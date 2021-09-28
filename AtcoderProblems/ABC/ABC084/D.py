def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)

def get_sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0] # pの倍数を削ぎ落とす


import pdb
import math
from itertools import accumulate

Q = int(input())
primes = get_sieve_of_eratosthenes(10**5)
imitate_2017 = [0] * 10**5
for i in range(len(primes)):
    if (primes[i]+1)//2 in primes:
        imitate_2017[primes[i]] = 1

acc = list(accumulate(imitate_2017))
for _ in range(Q):
    l, r = int_sp()
    print(acc[r]-acc[l-1])
