def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

N = int(input())
total = []
for _ in range(N):
    t, l, r = int_sp()
    if t == 1:
        total.append((l, r))
    elif t == 2:
        total.append((l, r-0.1))
    elif t == 3:
        total.append((l+0.1, r))
    elif t == 4:
        total.append((l+0.1, r-0.1))

cnt = 0
#pdb.set_trace()
for i, l1r1 in enumerate(total):
    l1 = l1r1[0]
    r1 = l1r1[1]
    for l2, r2 in total[i+1:]:
        if max(l1, l2) <= min(r1, r2):
            cnt += 1
print(cnt)


