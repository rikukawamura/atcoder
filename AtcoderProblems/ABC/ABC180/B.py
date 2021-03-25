import math

N = int(input())
X = list(map(int, input().split()))
abs_X = [abs(x) for x in X]
abs_2_X = [abs(x)**2 for x in X]
manhattan = sum(abs_X)
euclide = math.sqrt(sum(abs_2_X))
tyebu = max(abs_X)

print(manhattan)
print(euclide)
print(tyebu)