import pdb

r = 5
lattices = [(x**2 + y**2, x, y) for x in range(1, r) \
        for y in range(1, r) if x**2 + y**2 < r**2]
lattices.sort()
for x in lattices:
    print x