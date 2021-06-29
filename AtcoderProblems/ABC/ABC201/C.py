def int_sp():
    return map(int, input().split())

def li_int_sp():
    return list(map(int, input().split()))

# リストのリストの単一の要素を抽出 (リストのset)
# [[1, 1], [0, 1], [0, 1], [0, 0], [1, 0], [1, 1], [1, 1]] -> [[1, 1], [0, 1], [0, 0], [1, 0]]
def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]

# ----------------------------------------------------------------------------------------------------------
import pdb
import itertools

S = list(input())

maru = []
hatena = []
for i, s in enumerate(S):
    if s == 'o':
        maru.append(i)
    elif s == '?':
        hatena.append(i)

hatena = hatena + maru

if len(maru) > 4:
    print(0)
    exit()
else:
    seen = []
    for i in list(itertools.combinations_with_replacement(hatena, 4-len(maru))):
        for j in get_unique_list(list(itertools.permutations(maru + list(i)))):
            seen.append(j)
print(len(seen))




