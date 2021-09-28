def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)

import pdb
import math
X = int(input())
if 0 <= X < 40:
    print(40-X)
elif 40 <= X < 70:
    print(70-X)
elif 70 <= X < 90:
    print(90-X)
else:
    print('expert')