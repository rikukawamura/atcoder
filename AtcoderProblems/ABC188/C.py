N = int(input())
rates = list(map(int, input().split()))

left_block_winner = max(rates[:2**(N-1)])
right_block_winner = max(rates[2**(N-1):])

for i in range(len(rates)):
    if left_block_winner < right_block_winner:
        if rates[i] == left_block_winner:
            print(i+1)
    else:
        if rates[i] == right_block_winner:
            print(i+1)
