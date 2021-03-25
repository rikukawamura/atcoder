a, b = map(int, input().split())

a_b = str(a)*b
b_a = str(b)*a

print(min(a_b, b_a))