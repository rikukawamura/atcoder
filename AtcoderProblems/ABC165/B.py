import pdb

#小数の計算は避ける（after contestのサンプルがWAとなる）
x = int(input())
init = 100
nen = 0
while init < x:
    init *= 101
    init = int(init//100)
    nen += 1
print(nen)