import pdb

n = int(input())
oturi = 1000-n
coins = [500, 100, 50, 10, 5, 1]
output = 0
for coin in coins:
    #pdb.set_trace()
    output += oturi // coin
    oturi = oturi - coin*(oturi // coin)

print(output)