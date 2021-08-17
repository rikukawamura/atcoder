def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
A = []
N = int(input())
for _ in range(N):
    a = int(input())
    A.append(a)

brighted = [0]*N
brighted[0] = 1
cnt = 0
tmp = A[0]-1
while True:
    #pdb.set_trace()
    cnt += 1
    if tmp == 1:
        print(cnt)
        exit()
    elif brighted[tmp] != 0:
        print(-1)
        exit()
    brighted[tmp] = 1
    tmp = A[tmp]-1


