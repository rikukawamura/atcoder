def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

N, K = int_sp()
S = [int(input()) for _ in range(N)]

if 0 in S:
    print(N)
else:
    r, ans, tmp = 0, 0, 1
    for l in range(N):
        pdb.set_trace()
        while r < N and tmp*S[r] <= K:
            tmp *= S[r]
            r += 1
        ans = max(ans, r-l)
        if l == r:
            r += 1
        else:
            tmp //= S[l]
    print(ans)