import itertools

lists = [1, 3, 5 ,7, 9]
cumsum = itertools.accumulate(lists)
print(list(cumsum))