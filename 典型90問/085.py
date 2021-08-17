def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

import pdb
from itertools import combinations, product
prime_list = []
K = int(input())
primes = make_divisors(K)


cnt = 0
for i in product(primes, repeat=2):
    c = K/(i[0]*i[1])
    if i[0] <= i[1] <= c and c.is_integer():
        cnt += 1

print(cnt)


