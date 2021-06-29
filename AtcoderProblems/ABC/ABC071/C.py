import pdb
import collections

N = int(input())
A = list(map(int, input().split()))
A_col = collections.Counter(A)

length = []
length2 = []
for key, val in zip(A_col.keys(), A_col.values()):
    if val >= 4:
        length2.append(key)
    if val >= 2:
        length.append(key)

length = sorted(length, reverse=True)
length2 = sorted(length2, reverse=True)
if len(length) < 2:
    print(0)
elif length2 != []:
    print(max(length[0]*length[1], length2[0]*length2[0]))
else:
    print(length[0]*length[1])

