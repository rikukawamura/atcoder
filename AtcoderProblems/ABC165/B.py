import pdb

x = int(input())
init = 100
nen = 0
while init < x:
    init *= 1.01
    init = int(init)
    nen += 1
print(nen)