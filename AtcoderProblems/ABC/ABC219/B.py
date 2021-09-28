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
S1 = input()
S2 = input()
S3 = input()
T = list(map(int, list(input())))
#pdb.set_trace()
output = []
for t in T:
    if t == 1:
        output.append(S1)
    elif t == 2:
        output.append(S2)
    else:
        output.append(S3)
print(''.join(output))