
x = int(input())
sosuu = [2]
A = 1000000
if x == 2:
    print(2)
    exit()

for L in range(3, A, 2): # 2 以外の素数は奇数なので
    if all(L % L2 != 0 for L2 in sosuu):  # すべての既存素数で割り切れなかったら素数
        sosuu.append(L)
        if L >= x:
            print(L)
            exit()