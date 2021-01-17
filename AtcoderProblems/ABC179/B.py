N = int(input())

count = 0
flag = True
for i in range(N):
    A, B = map(int, input().split())
    if A == B:
        count += 1
        if count == 3:
            print('Yes')
            flag = False
            break
    else:
        count = 0

if flag:
    print('No')