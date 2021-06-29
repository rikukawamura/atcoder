def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def main():
    import pdb


    N = int(input())
    A = sorted(li_int_sp())
    B = sorted(li_int_sp())
    output = 0
    for a, b in zip(A, B):
        output += abs(a-b)
    print(output)



if __name__ == '__main__':
    main()