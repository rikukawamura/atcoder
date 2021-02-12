N = int(input())

total = 0
for i in range(1, N):
    if (N-i) % i != 0:
        total += ((N-i) // i) + 1
    else:
        total += (N-i) // i
print(total)