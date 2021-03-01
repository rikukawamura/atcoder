n, m = map(int, input().split())
a = list(map(int, input().split()))
total_a = sum(a)
threshold = total_a / (4*m)

count = 0
for i in a:
    if i >= threshold:
        count += 1
    if count == m:
        print('Yes')
        exit()
print('No')
