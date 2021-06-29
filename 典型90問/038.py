import math

def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def my_lcm(x, y):
    return (x * y) // math.gcd(x, y)

def main():
    import pdb


    A, B = int_sp()
    x = my_lcm(A,B)
    if x <= 10**18:
        print(x)
    else:
        print('Large')


if __name__ == '__main__':
    main()