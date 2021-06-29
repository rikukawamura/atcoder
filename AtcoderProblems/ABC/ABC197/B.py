import pdb

H, W, X, Y = map(int, input().split())
X = X - 1
Y = Y - 1
S = [input() for _ in range(H)]

#pdb.set_trace()
count = 1

i = 1
while True:
    if X-i < 0:
        break
    if S[X-i][Y] == '#':
        break
    else:
        count += 1
    i+=1

i = 1
while True:
    if X+i >= H:
        break
    if S[X+i][Y] == '#':
        break
    else:
        count += 1
    i+=1

i = 1
while True:
    if Y-i < 0:
        break
    if S[X][Y-i] == '#':
        break
    else:
        count += 1
    i+=1

i = 1
while True:
    if Y+i >= W:
        break
    if S[X][Y+i] == '#':
        break
    else:
        count += 1
    i+=1

print(count)