import pdb

N = int(input())
S = input().strip()

lr_counter = []
l_counter = 0
r_counter  = 0
for i in S:
    if i == 'W':
        l_counter += 1
    else:
        r_counter += 1
    lr_counter.append([l_counter, r_counter])


if S[0] == 'W':
    min_val = lr_counter[-1][1]
else:
    min_val = lr_counter[-1][1] - 1


for i in range(1, N):
    if i == 'W':
        l = lr_counter[i-1][0]
        r = lr_counter[-1][1] - lr_counter[i][1]
        min_val = min(l+r, min_val)
    else:
        l = lr_counter[i][0]
        r = lr_counter[-1][1] - (lr_counter[i][1])
        min_val = min(l + r, min_val)
print(min_val)
