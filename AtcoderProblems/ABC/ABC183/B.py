import pdb

s_x, s_y, g_x, g_y = map(int, input().split())
x = ((g_x-s_x)/(-g_y-s_y) * -s_y) + s_x
print(x)