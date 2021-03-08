import pdb
import collections as col
import itertools as ite

N = int(input())
H = list(map(int, input().split()))
H = list(ite.groupby(H))
#　初期値設定
init = H[0][0]
for key, group in H[1:]:
    if key < init:
        print('No')
        exit()
    elif key > init:
        init = key - 1
    else:
        init = key
print('Yes')



