def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N = int(input())
S = li_int_sp()
T = li_int_sp()

output = [[] for i in range(N)]
for i, t in enumerate(T):
    output[i].append(t)
#pdb.set_trace()

i = 0
tmp = T[0]
for s in S:
    #pdb.set_trace()
    tmp += s
    output[(i+1)%(N)].append(tmp)
    i+=1
#pdb.set_trace()

i = 0
for s, t in zip(S, T):
    #pdb.set_trace()
    output[(i+1)%(N)].append(s+t)
    i+=1
#pdb.set_trace()
for i in output:
    print(min(i))

