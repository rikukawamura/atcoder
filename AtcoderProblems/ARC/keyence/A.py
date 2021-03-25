import pdb

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

k=0
tmp = []
for n in range(0, N):
    for i in range(k, n+1):
        for j in range(0, i+1):
            #pdb.set_trace()
            tmp.append(A[j] * B[i])
        k += 1
    print(max(tmp))

