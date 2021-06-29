import pdb

A, B = map(int, input().split())

A_list = list(range(1, A+1))
B_list = list(range(1, B+1))

if A >= B:
    B_list = []
    A_sum = sum(A_list)
    for i in range(1, B):
        B_list.append(i)
    B_list.append(A_sum-sum(B_list))
    B_list = list(map(lambda x: -x, B_list))
elif A < B:
    A_list = []
    B_sum = sum(B_list)
    for i in range(1, A):
        A_list.append(i)
    A_list.append(B_sum-sum(A_list))
    B_list = list(map(lambda x: -x, B_list))
print(*A_list + B_list)