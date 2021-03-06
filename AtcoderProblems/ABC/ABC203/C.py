from math import factorial
import pdb


# ----------------------------------------------------------------------------------------------------------

def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))


def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


# リストのリストの単一の要素を抽出 (リストのset)
# [[1, 1], [0, 1], [0, 1], [0, 0], [1, 0], [1, 1], [1, 1]] -> [[1, 1], [0, 1], [0, 0], [1, 0]]
def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr
# ----------------------------------------------------------------------------------------------------------
#　尺取り法

def main():
    from collections import defaultdict
    N, K = int_sp()
    friends = defaultdict(int)
    for _ in range(N):
        A, B = int_sp()
        friends[A] += B
    friends = sorted(friends.items(), key=lambda x:x[0], reverse=False)

    #pdb.set_trace()
    flag = False
    proceed = 0
    tmp = 0
    for village, money in friends:
        if K >= (village-tmp):
            K -= (village-tmp)
            K += money
            proceed = village
            tmp = village
        else:
            flag = True
            proceed = tmp + K
    #pdb.set_trace()

    if flag == False:
        print(proceed+K)
    else:
        print(proceed)



if __name__ == '__main__':
    main()