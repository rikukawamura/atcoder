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
import math
#print(math.sqrt(10**5)*10**5*2)

N, M = int_sp()
A = set(li_int_sp())
B = set(list(range(1, M+1)))

A_div = []
# Aの約数を列挙
for a in A:
    #pdb.set_trace()
    A_div += make_divisors(a)
A_div = set(A_div)
#pdb.set_trace()

cnt = 0
x = []
for b in B:
    #pdb.set_trace()
    if len(set(make_divisors(b)) & set(A_div)) == 1:
        x.append(b)
        cnt += 1


print(cnt)
for i in x:
    print(i)



