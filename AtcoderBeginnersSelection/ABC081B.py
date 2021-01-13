num_index = int(input())
x = input().split()

count = -1
flag = True

while flag:
    count += 1
    for i in range(len(x)):
        if int(x[i]) % 2 == 1:
            flag = False
        x[i] = int(x[i]) / 2


print(count)