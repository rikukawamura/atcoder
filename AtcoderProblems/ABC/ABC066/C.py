import pdb

N = int(input())
A = list(map(int, input().split()))

pre = []
post = []
for i, n in enumerate(range(N), 1):
    if i % 2 == 1:
        pre.append(A[n])
    else:
        post.append(A[n])
if i % 2 == 0:
    print(*post[::-1]+pre)
else:
    print(*pre[::-1]+post)