N = int(input())
A = list(map(int, input().split()))

output = 1
if 0 in A:
    print(0)
    exit()
else:
    for a in A:
        output *= a
        if output > 10 ** 18:
            print(-1)
            exit()
print(output)