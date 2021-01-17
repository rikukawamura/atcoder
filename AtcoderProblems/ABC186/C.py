N = int(input())

ten, eight = [], []
for i in range(1, N+1):
    i = str(i)
    if '7' in i:
        ten.append(i)
    elif '7' in str(oct(int(i))):
        eight.append(i)

output = set(ten+eight)
print(N - len(output))
