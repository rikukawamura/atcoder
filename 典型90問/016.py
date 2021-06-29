def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def main():
    import pdb


    N = int(input())
    A, B, C = int_sp()

    min_val = float('INF')
    for i in range(10**4):
        for j in range(10**4-i):
            k = (N-A*i-B*j)//C
            if (A*i+B*j+C*k) == N and k >= 0:
                min_val = min(min_val, i+j+k)
    print(min_val)


if __name__ == '__main__':
    main()