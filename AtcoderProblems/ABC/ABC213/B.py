def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N = int(input())
A = li_int_sp()
lists = []
for i, a in enumerate(A):
    lists.append([a, i])
#pdb.set_trace()
lists = sorted(lists)
print(lists[-2][1]+1)
