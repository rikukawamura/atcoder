def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def main():
    import pdb
    import math

    a,b,c = int_sp()
    if a < pow(c,b):
        print('Yes')
    else:
        print('No')



if __name__ == '__main__':
    main()