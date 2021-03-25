import pdb

n = int(input())
x = list(map(int, input().split()))

ave = round(sum(x) / len(x))
#pdb.set_trace()

output = 0
for i in x:
    output += (abs(i - ave))**2

print(output)