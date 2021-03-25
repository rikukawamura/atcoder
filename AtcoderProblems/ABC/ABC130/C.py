import pdb

W, H, x, y = map(int, input().split())

tyusin_x = W / 2
tyusin_y = H / 2

if x == tyusin_x and y == tyusin_y:
    print((W*H)/2, 1)
else:
    print((W*H)/2, 0)

