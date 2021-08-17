def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from collections import Counter

N = int_sp()
A = li_int_sp()
B = li_int_sp()
C = li_int_sp()

A_mod = Counter([x%46 for x in A])
B_mod = Counter([x%46 for x in B])
C_mod = Counter([x%46 for x in C])
#pdb.set_trace()

output = 0
for value_a, cnt_a in zip(A_mod.keys(), A_mod.values()):
    for value_b, cnt_b in zip(B_mod.keys(), B_mod.values()):
        for value_c, cnt_c in zip(C_mod.keys(), C_mod.values()):
            if (value_a+value_b+value_c) % 46 == 0:
                output += (cnt_a*cnt_b*cnt_c)
print(output)




