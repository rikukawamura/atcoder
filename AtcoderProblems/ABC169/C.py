import pdb

a, b = map(str, input().split())
a = int(a)
b = int(b[0] + b[2] + b[3])
c = a*b
print(int(c//100))