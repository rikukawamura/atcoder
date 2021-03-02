import pdb


n = int(input())
a = list(map(int, input().split()))
b = set(a)

total = []
for th in b:
    c = [x for x in a if x >= th]
    total.append(th * len(c))

print(max(total))