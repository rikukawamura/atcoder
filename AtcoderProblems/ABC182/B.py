N = int(input())
A = list(map(int, input().split()))

output = 0
for i in range(2, 1001):
    count = 0
    for j in A:
        if j % i == 0:
            count += 1
    if count > output:
        output = count
        number = i

print(number)