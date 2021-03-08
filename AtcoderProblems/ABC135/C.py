import pdb

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# モンスターの総合数
total_A = sum(A)
for i in range(len(B)):
    if B[i] >= A[i] + A[i+1]:
        A[i] = 0
        A[i+1] = 0
    elif B[i] >= A[i] and B[i] < A[i] + A[i+1]:
        A[i+1] = A[i+1] - (B[i] - A[i])
        A[i] = 0
    else:
        A[i] = A[i] - B[i]
    #print(A)
# モンスターの総合数 - 残っているモンスター = 倒したモンスター数
print(total_A - sum(A))
