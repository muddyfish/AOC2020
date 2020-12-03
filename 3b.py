import operator
from functools import reduce

trees = [0, 0, 0, 0, 0]


def prod(iterable):
    return reduce(operator.mul, iterable, 1)


with open("3.txt") as f:
    lines = [i.strip() for i in f.readlines()[1:]]

for i, mult in enumerate([1, 3, 5, 7]):
    for offset, line in enumerate(lines, start=1):
        trees[i] += line[(offset*mult) % len(line)] == "#"
for offset in range(1, len(lines), 2):
    trees[-1] += lines[offset][(offset//2+1) % len(lines[0])] == "#"

print(prod(trees))
