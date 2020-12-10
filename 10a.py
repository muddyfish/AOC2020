from collections import Counter


def deltas(inp):
    return [inp[i] - num for i, num in enumerate(inp[:-1], 1)]


with open("10.txt") as f:
    adaptors = [i for i in map(int, f.readlines())]

adaptors.sort()
counts = Counter(deltas(adaptors))

print((counts[1]+1) * (counts[3]+1))
