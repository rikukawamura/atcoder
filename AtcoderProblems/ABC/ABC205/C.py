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
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


# ----------------------------------------------------------------------------------------------------------
def main():

    A, B, C = int_sp()
    z = C % 2
    abs_A = abs(A)
    abs_B = abs(B)


    if A == B:
        print('=')
        exit()
    if A > B and B >= 0:
        print('>')
    elif B > A and A >= 0:
        print('<')
    elif z == 1 and A < 0 and B < 0:
        if abs_A > abs_B:
            print('<')
        else:
            print('>')
    elif z == 1 and A < 0 and B >= 0:
        print('<')
    elif z == 1 and A >= 0 and B < 0:
        print('>')
    elif z == 0:
        if abs_A > abs_B:
            print('>')
        elif abs_A == abs_B:
            print('=')
        else:
            print('<')



if __name__ == '__main__':
    main()