import pdb
import math


a, b, h, m = map(int, input().split())
a_angle = 30 * h + m / 2 # m/2を足すの忘れてた
b_angle = 6 * m

angle = abs(a_angle-b_angle)
c = math.sqrt(a**2 + b**2 - math.cos(math.radians(angle)) * 2 * a * b)
print(c)
