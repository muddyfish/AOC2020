from functools import lru_cache


def deltas(inp):
    return [inp[i] - num for i, num in enumerate(inp[:-1], 1)]


with open("10.txt") as f:
    adaptors = [i for i in map(int, f.readlines())]
adaptors.append(0)
adaptors.sort()

end = adaptors[-1]
reachable = {k: [j for j in adaptors[i+1:i+4] if j <= k + 3] for i, k in enumerate(adaptors)}


@lru_cache(len(adaptors)+2)
def arrangements(start: int) -> int:
    if start == end:
        return 1
    return sum(map(arrangements, reachable[start]))


print(arrangements(0))
