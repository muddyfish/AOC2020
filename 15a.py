with open("15.txt") as f:
    first = [int(i) for i in f.readline().strip().split(",")]
    sequence = {j: i for i, j in enumerate(first[:-1])}

last = first[-1]
for turn in range(len(first), 30000000):
    sequence[last], last = turn - 1, turn - sequence.get(last, turn-1) - 1
print(last)
