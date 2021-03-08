import pdb

#　辞書の要素順に並び替える練習
n = int(input())
a = list(map(int, input().split()))

dic = {}

for i, j in enumerate(a, 1):
    dic[i] = j

sorted_dic = sorted(dic.items(), key=lambda x:x[1])

output = []
for i in sorted_dic:
    output.append(i[0])
print(*output)
