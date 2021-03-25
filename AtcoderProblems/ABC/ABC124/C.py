import pdb

S = list(map(int, list(input())))
X = [0 if x%2==0 else 1 for x in range(len(S))]
Y = [1 if x%2==0 else 0 for x in range(len(S))]

x_count = 0
y_count = 0
for s, x, y in zip(S, X, Y):
    if s != x:
        x_count += 1
    if s != y:
        y_count += 1
print(min(x_count, y_count))
