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
    questions = set("".join(group))
    group_total = sum(1 for q in questions if all(q in p for p in group))
    total += group_total

print(total)
