N = input()
x = sorted([int(i) for i in input().split()], reverse=True)

alice = 0
bob = 0

for i in range(len(x)):
    if i % 2 == 0:
        alice += int(x[i])
    else:
        bob += int(x[i])
print("{}".format(alice-bob))