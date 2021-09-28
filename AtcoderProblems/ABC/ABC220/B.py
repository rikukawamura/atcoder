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
K = int(input())
A, B = int_sp()
ten_A = int(str(A), K)
ten_B = int(str(B), K)
print(ten_A*ten_B)