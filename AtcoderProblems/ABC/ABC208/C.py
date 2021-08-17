def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

N, K = int_sp()
A = li_int_sp()

all_distribute = K // N
mod = K % N

ind_A = []
for ind, a in enumerate(A):
    ind_A.append([ind, a])
#pdb.set_trace()
ind_A = sorted(ind_A, reverse=False, key=lambda x: x[1])
ind_A = [[ind, all_distribute] for ind, a in ind_A]

for i in range(mod):
    ind_A[i][1] += 1

ind_A = sorted(ind_A, reverse=False, key=lambda x: x[0])

for i in ind_A:
    print(i[1])