import itertools

n = int(input())

x = [x for x in range(1, n+1) if (x % 3 != 0) and (x % 5 != 0)]
x = list(itertools.accumulate(x))
print(x[-1])