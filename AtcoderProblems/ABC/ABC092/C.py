def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

N = int(input())
A = li_int_sp()
A = [0]+A+[0]
idou_cost = 0
for i in range(len(A)-1):
    idou_cost += abs(A[i+1] - A[i])

for i in range(1, len(A)-1):
    #pdb.set_trace()
    if A[i-1] <= A[i] <= A[i+1]:
        print(idou_cost)
    elif A[i-1] <= A[i] and A[i+1] < A[i]:
        print(idou_cost-abs(A[i-1]-A[i])*2)
    elif A[i] < A[i-1] and A[i] <= A[i+1]:
        print(idou_cost-abs(A[i+1]-A[i])*2)
    else:
        print(idou_cost-abs(A[i-1]-A[i])-abs(A[i+1]-A[i])+abs(A[i+1]-A[i-1]))
