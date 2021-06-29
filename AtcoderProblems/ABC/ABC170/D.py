import pdb


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


N = int(input())
A = list(map(int, input().split()))

count = 0
for i, a in enumerate(A):
    x = make_divisors(a)
    if (set(x) & set(A[:i] + A[i+1:])):
        #pdb.set_trace()
        count += 1

print(len(A)-count)