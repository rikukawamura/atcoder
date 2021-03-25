N = int(input())

x = 10**N - 9**N - 9**N + 8**N
y = 10**9+7
if N == 1:
    print(0)
else:
    print(x % y)