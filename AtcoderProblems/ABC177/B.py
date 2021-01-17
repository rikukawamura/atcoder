S = list(input())
T = list(input())
output = 0
count = 0
for i in range(len(S)-len(T)+1):
    for s, t in zip(S[i:len(T)+i], T):
        for x, y in zip(s, t):
            if x == y:
                count += 1
        if count >= output:
            output = count
    count = 0

print(len(T)-output)

