def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N, K = int_sp()
R, S, P = int_sp()
T = input()
hands = []

total = 0
for t in T[:K]:
    if t == 'r':
        total += P
        hands.append('p')
    elif t == 's':
        total += R
        hands.append('r')
    else:
        total += S
        hands.append('s')

pre_K = 0
for t in T[K:]:
    #pdb.set_trace()
    if t == 'r':
        if hands[pre_K] == 'p':
            hands.append('')
        else:
            total += P
            hands.append('p')
    elif t == 's':
        if hands[pre_K] == 'r':
            hands.append('')
        else:
            total += R
            hands.append('r')
    else:
        if hands[pre_K] == 's':
            hands.append('')
        else:
            total += S
            hands.append('s')
    pre_K += 1
print(total)
