def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

N, K = int_sp()
H = []
S = set()

n = N
start = 0
while True:
    if n in S:
        start = H.index(n)
        break
    H.append(n)
    S.add(n)
    x = sum(map(int, list(str(n))))
    z = (x+n)%(10**5)
    n = z

if K < len(H):
    print(H[K])
else:
    print(H[(K-start) % (len(H) - start) + start])








