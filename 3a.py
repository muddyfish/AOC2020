trees = 0

with open("3.txt") as f:
    lines = [i.strip() for i in f.readlines()[1:]]

for offset, line in enumerate(lines, start=1):
    trees += line[(offset*3) % len(line)] == "#"

print(trees)
