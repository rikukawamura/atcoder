'''
# 自分の回答 (TLE連発)
N, Y = input().split()
N = int(N)
Y = int(Y)
x_list = sorted([x*10000 for x in range(N+1)], reverse=True)
y_list = sorted([x*5000 for x in range(N+1)], reverse=True)
z_list = sorted([x*1000 for x in range(N+1)], reverse=True)

output_flag = False
roop_flag = False

for i in x_list:
    for j in y_list:
        for k in z_list:
            if i+j+k == Y:
                num_x = i / 10000
                num_y = j / 5000
                num_z = k / 1000
                if num_x+num_y+num_z == N:
                    print("{} {} {}".format(int(num_x), int(num_y), int(num_z)))
                    output_flag = True
                    roop_flag = True
                    break
        if roop_flag:
            break
    if roop_flag:
        break

if not output_flag:
    print("-1 -1 -1")
'''

# https://ikatakos.com/pot/programming_algorithm/contest_history/atcoder/2018/0107_abc085を参考にさせて頂いた
N, Y = input().split()
N = int(N)
Y = int(Y)

output_flag = False
roop_flag = False

for i in range(N+1):
    for j in range(N-i+1):
        if 10000*i + 5000*j + 1000*(N-i-j) == Y:
            output_flag = True
            roop_flag = True
            print("{} {} {}".format(i, j, N-i-j))
            break
    if roop_flag:
        break

if not output_flag:
    print("-1 -1 -1")