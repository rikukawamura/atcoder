def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from math import sin, cos, atan, radians, degrees, sqrt

T = int(input())
L, X, Y = li_int_sp()
Q = int(input())
theta = 360/T # 1分間の角度の遷移
radius = L/2 # 半径


for _ in range(Q):
    E = int(input())
    y = radius * -cos(radians(E*theta-90))
    z = radius * sin(radians(E*theta-90)) + radius
    senbun = sqrt((X-0)**2 + (Y-y)**2 + (0-0)**2)
    fukaku = atan(z/senbun)
    print(degrees(fukaku))




