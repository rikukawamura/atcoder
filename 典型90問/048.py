def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

N, K = int_sp()

per_score = []
for _ in range(N):
    A, B = int_sp()
    per_score.append(B)
    per_score.append(A-B)
per_score = sorted(per_score, reverse=True)
print(sum(per_score[:K]))




