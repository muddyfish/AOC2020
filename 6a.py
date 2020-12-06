with open("6.txt") as f:
    lines = [[]]
    for i in f.readlines():
        i = i.strip()
        if i:
            lines[-1].append(i)
        else:
            lines.append([])

total = 0
for group in lines:
    group_total = len(set("".join(group)))
    total += group_total

print(total)
