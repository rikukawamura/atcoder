"""
ポラード・ロー法で素因数分解
"""

# 最大公約数
def gcd(a, b):
    if a<b:
        return gcd(b, a)
    while b>0:
        a, b = b, a%b
    return a

# 素数判定
def isprime(n):
    if n<2:
        return False
    for m in range(2, int(n**0.5+1)):
        if n%m==0:
            return False
    return True

# 疑似乱数発生器（らしい）
def f(n):
    ret = n**2+seed
    return ret%target

# 素数になるまで割る？
def factoring(n, _seed = 3):
    if isprime(n):
        return n
    x, y, d = 2, 2, 1
    tmp = n
    seed = _seed
    while d==1:
        x = f(x)
        y = f(f(y))
        dif = x-y if x>y else y-x
        d = gcd(dif, tmp)
        seed+=1

    seed = 0
    if(d%2==0):
        return 2
    if isprime(d) is False:
        return factoring(d, seed+1)
    return factoring(d, 1)

# メイン
def factors():
    dic = {}
    tmp = target
    if(isprime(tmp)):
        dic[tmp] = 1
        return dic

    ret = factoring(tmp)
    while tmp/ret is not 0:
        if ret in dic.keys():
            dic[ret]+=1
        else:
            dic[ret]=1
        tmp = int(tmp/ret)
        if tmp==1:
            break
        ret = factoring(tmp)

    return dic

def main():
    T = int(input())
    case = list(map(int, input().split()))
    for i in case:
        target = i
        seed = 0
        print(factors())

if __name__=='__main__':
    main()