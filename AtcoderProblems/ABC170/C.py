import pdb

X, N = map(int, input().split())
P = list(map(int, input().split()))

total_list = list(range(1, 101))
Q = [0] + list(set(total_list) - set(P))
pdb.set_trace()

tmp = 101
for i in Q:
    mini = abs(X - i)
    if mini < tmp:
        tmp = mini
        output = i

print(output)