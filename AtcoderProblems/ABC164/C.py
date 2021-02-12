from collections import Counter

n = int(input())
print(len(Counter([input() for i in range(n)])))




