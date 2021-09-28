def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N, K = int_sp()
A = li_int_sp()
total = sum(A[0:K])
tmp = sum(A[0:K])

for i in range(K, N):
    tmp += A[i]
    tmp -= A[i-K]
    total += tmp
print(total)
