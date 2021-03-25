A, B = input().split()

sum_A = int(A[0]) + int(A[1]) + int(A[2])
sum_B = int(B[0]) + int(B[1]) + int(B[2])

if sum_A >= sum_B:
    print(sum_A)
else:
    print(sum_B)