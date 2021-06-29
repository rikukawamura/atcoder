import pdb
import itertools


N = int(input())
S = sorted([int(input()) for _ in range(N)], reverse=False)

non_ten = []
ten = []

for s in S:
    if s % 10 == 0:
        ten.append(s)
    else:
        non_ten.append(s)

ten = sorted(ten)
non_ten = sorted(non_ten)

total = sum(ten)+sum(non_ten)
'''
1. 総合点が10の倍数且つ，10の倍数でない問題がある場合
2. 総合点が10の倍数且つ，10の倍数でない問題がない場合
3. 総合点が10の倍数でない
の三つに場合分け
'''
if total % 10 == 0 and non_ten != []:
    print(total-non_ten[0])
elif total % 10 == 0 and non_ten == []:
    print(0)
else:
    print(total)