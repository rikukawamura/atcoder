N = int(input())

x = []
for i in range(1, N):
    a = i
    b = N-a
    x.append([a, b])
print(len(x))