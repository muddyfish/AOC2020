with open("6.txt") as f:
    lines = [i.split("\n") for i in f.read().split("\n\n")]

total = 0
for group in lines:
    questions = set("".join(group))
    total += sum(all(q in p for p in group) for q in questions)

print(total)
