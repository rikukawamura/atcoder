import pdb

N = int(input())
H = list(map(int, input().split()))
H.insert(0, 0)
H.extend([0])

water_count = 0
while not all([True if x <= 0 else False for x in H]):
    need_water = []
    zero_index = [i for i, x in enumerate(H) if x == 0]
    start = 0
    #pdb.set_trace()
    if zero_index == []:
        water_count += 1
        H = list(map(lambda x: x - 1 if x > 0 else x, H))
        continue
    for i in zero_index:
        if H[start:i] != []:
            need_water.append(H[start:i])
        start = i+1
    water_count += len(need_water)
    H = list(map(lambda x: x - 1 if x > 0 else x, H))
print(water_count)


    
