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
#print(math.sqrt(10**5)*(10**5)*2)

N, M = int_sp()
A = set(li_int_sp())
ng = [False]*(10**5+1)

# Aの約数を列挙
for a in A:
    x = make_divisors(a)
    for i in x:
        ng[i] = True

for p in range(2, M+1):
    if ng[p] == True:
        for q in range(p+p, M+1, p):
            ng[q] = True

ng[0] = True
ng[1] = False

output = []
for i, j in enumerate(ng[:M+1]):
    if j != True:
        output.append(i)


print(len(output))
for i in output:
    print(i)



