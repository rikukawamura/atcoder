def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N, x = int_sp()
A = li_int_sp()

cnt = 0
for i in range(N-1):
    #pdb.set_trace()
    total = A[i+1]+A[i]
    if total <= x: # 二つの合計がx以上なら無視
        continue
    diff = total - x  # 減らさなければならない数
    tmp = 0
    for j in reversed(range(2)):
        tmp = A[i+j]-diff
        if tmp <= 0:
            diff -= A[i+j]
            cnt += A[i+j]
            A[i+j] = 0
        else:
            cnt += (A[i+j]-tmp)
            A[i+j] = tmp
        if A[i+1] + A[i] <= x:
            break
#print(A)
print(cnt)