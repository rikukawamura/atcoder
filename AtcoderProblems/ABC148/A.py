a = int(input())
b = int(input())
choices = [1, 2, 3]
choices.remove(a)
choices.remove(b)
print(*choices)