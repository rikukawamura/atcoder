import math
import pdb

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

n = int(input())
if n == 2:
    x, y = map(int, input().split())
    a = make_divisors(x)
    b = make_divisors(y)
    kinds = set(a+b)
    for i in kinds:
        if i in a and i in b:
            print(i)
elif n == 3:
    x, y, z = map(int, input().split())
    a = make_divisors(x)
    b = make_divisors(y)
    c = make_divisors(z)
    kinds = set(a + b + c)
    for i in kinds:
        if i in a and i in b and i in c:
            print(i)

