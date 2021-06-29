def main():
    N, K = int_sp()
    friends = [0] * 2*(10**5)
    for _ in range(N):
        A, B = int_sp()
        friends[A] += B

    #pdb.set_trace()

    village = 0
    while K > 0:
        pdb.set_trace()
        K -= 1
        village += 1
        K += friends[village]

    print(village)