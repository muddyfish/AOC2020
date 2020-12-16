import re

constraint_regex = re.compile(r".*: (\d+)-(\d+) or (\d+)-(\d+)")
constraints = []
nearby = []


def is_valid(field: int) -> bool:
    for a,b, c,d in constraints:
        for l, h in [(a, b), (c, d)]:
            if l <= field <= h:
                return True
    return False


with open("16.txt") as f:
    constraint_str, my_ticket_str, nearby_str = f.read().split("\n\n")
    for line in constraint_str.split("\n"):
        constraints.append([int(i) for i in constraint_regex.match(line).groups()])
    for line in nearby_str.split("\n")[1:]:
        nearby.append([int(i) for i in line.split(",")])

invalid_fields = sum(f for i in nearby for f in i if not is_valid(f))

print(invalid_fields)
