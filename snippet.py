import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

# input = sys.stdin.readline
#def i_input(): return int(input())
def int_map(): return map(int, input().split())
def int_list(): return list(int_map())
def int_ver(N): return [int(input()) for _ in range(N)]
def int_ver_list(N): return [int_list() for _ in range(N)]
#def s_input(): return input()
#def s_map(): return input().split()
#def s_list(): return list(s_map())
def s_row(N): return [input() for _ in range(N)]
def s_row_str(N): return [list(input().split()) for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def main():
    n = i_input()
    a, b = i_map()
    num_list = i_list()

    print()

if __name__ == '__main__':
    main()