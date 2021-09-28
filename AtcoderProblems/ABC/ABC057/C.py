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
N = int(input())
div = make_divisors(N)
#pdb.set_trace()

min_val = float('INF')
for i in div:
    if N%i == 0:
        #pdb.set_trace()
        x = N//i
        tmp = max(len(list(str(x))), len(list(str(i))))
        min_val = min(min_val, tmp)
print(min_val)

