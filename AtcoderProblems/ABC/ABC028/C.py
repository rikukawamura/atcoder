import pdb
import itertools

X = list(map(int, input().split()))

output = []
for iter in list(itertools.combinations(X, 3)):
    output.append(sum(iter))

output = sorted(output, reverse=True)
print(output[2])


