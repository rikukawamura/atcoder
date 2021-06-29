import pdb

S = list(input())
rev_S = S[::-1]

count = 0
#pdb.set_trace()
if len(S) % 2 == 0:
    for i in range(len(S)//2):
        if S[i] != rev_S[i]:
            count += 1
else:
    for i in range(len(S)//2 + 1):
        if S[i] != rev_S[i]:
            count += 1

print(count)