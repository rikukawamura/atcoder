x = int(input())
coins = [500, 5]
happy = [1000, 5]
a = 0
b = 0
for coin, happy in zip(coins, happy):
    a = x // coin
    x = x - (coin * a)
    b += a * happy
print(b)