def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

H, W = int_sp()

A, B = [], [] # Aが変動，Bが正解
for _ in range(H):
    A.append(li_int_sp())
for _ in range(H):
    B.append(li_int_sp())

if A == B:
    print('Yes')
    print(0)
    exit()

cnt = 0
for i in range(H-1):
    for j in range(W-1):
        #pdb.set_trace()
        if A[i][j] < B[i][j]:
            diff = abs(A[i][j]-B[i][j])
            A[i][j] += diff
            A[i+1][j] += diff
            A[i][j+1] += diff
            A[i+1][j+1] += diff
            cnt += diff
        elif A[i][j] > B[i][j]:
            diff = abs(A[i][j]-B[i][j])
            A[i][j] -= diff
            A[i+1][j] -= diff
            A[i][j+1] -= diff
            A[i+1][j+1] -= diff
            cnt += diff
        else:
            continue


        if A == B:
            print('Yes')
            print(cnt)
            exit()
print('No')