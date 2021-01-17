import pdb

N = int(input())
attend_num = 2^N
rate = list(map(int, input().split()))
index = list(range(1, len(rate)+1))
dictionary = {key: val for key, val in zip(rate, index)}
tmp_rate = list(map(int, input().split()))


for i in range(0,N+1,2):
    del_idx = min((rate[i], rate[i+1]))
    del tmp_rate[del_idx]

pdb.set_trace()
print(tmp_rate)