def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
import bisect

N = int(input())
S = input()

R = []
G = []
B = []

for i, s in enumerate(S):
    if s=='R':
        R.append(i)
    elif s=='G':
        G.append(i)
    else:
        B.append(i)

len_B = len(B)
cnt = 0
for r in R:
    for g in G:
        tmp = 0
        dist = abs(r-g)
        max_val = max(r, g)+dist
        min_val = min(r, g)-dist
        mid_val =(r+g)/2
        bi_max = bisect.bisect_left(B, max_val)
        bi_min = bisect.bisect_left(B, min_val)
        bi_mid = bisect.bisect_left(B, mid_val)
        if (0 <= bi_max <= len_B-1):
            if B[bi_max] == bi_max:
                tmp+=1
        if (0 <= bi_min <= len_B-1):
            if B[bi_min] == bi_min:
                tmp+=1
        if (0 <= bi_mid <= len_B-1):
            if B[bi_mid] == bi_mid:
                tmp+=1
        cnt += len_B-tmp

print(cnt)
