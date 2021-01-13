x = input().split()
N = int(x[0])
A = int(x[1])
B = int(x[2])

output = 0

for i in range(1, N+1):
    sum = 0
    list_i = list(str(i))
    for j in list_i:
        sum += int(j)
    if sum >= A and sum <= B:
        output += i

print(output)