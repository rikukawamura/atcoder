import pdb
import collections
import itertools
from scipy.special import comb

N = int(input())
S = [input().strip() for _ in range(N)]

M, A, R, C, H = 0, 0, 0, 0, 0
for s in S:
    if s[0] == 'M':
        M += 1
    elif s[0] == 'A':
        A += 1
    elif s[0] == 'R':
        R += 1
    elif s[0] == 'C':
        C += 1
    elif s[0] == 'H':
        H += 1

march = []
if M!=0:
    march.append(M)
if A!=0:
    march.append(A)
if R!=0:
    march.append(R)
if C!=0:
    march.append(C)
if H!=0:
    march.append(H)

total = 0
for i in list(itertools.combinations(march, 3)):
    total += i[0]*i[1]*i[2]
print(total)

