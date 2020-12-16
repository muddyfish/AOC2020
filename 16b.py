from typing import Set
from collections import Counter
import re

constraint_regex = re.compile(r"(.*): (\d+)-(\d+) or (\d+)-(\d+)")
constraints = []
nearby = []
my_ticket = []


def valid_fields(field: int) -> Set[str]:
    rtn = set()
    for name, a, b in constraints:
        for l, h in [a, b]:
            if l <= field <= h:
                rtn.add(name)
    return rtn


with open("16.txt") as f:
    constraint_str, my_ticket_str, nearby_str = f.read().split("\n\n")
    for line in constraint_str.split("\n"):
        a,b,c,d,e = constraint_regex.match(line).groups()
        constraints.append((a, (int(b), int(c)), (int(d), int(e))))
    for line in nearby_str.split("\n")[1:]:
        nearby.append([int(i) for i in line.split(",")])
    my_ticket = [int(i) for i in my_ticket_str.split("\n")[1].split(",")]

valid_tickets = [ticket for ticket in nearby if all(valid_fields(f) for f in ticket)]


possible_fields = []
for field_list in zip(*valid_tickets):
    possible = set(name for name, _, _ in constraints)
    for field in field_list:
        possible &= valid_fields(field)
    possible_fields.append(possible)

pos_names = {}

field_counts = Counter(j for i in possible_fields for j in i)
count_fields = {v: k for k, v in field_counts.items()}
for id in range(1, len(count_fields)+1):
    field_name = count_fields[id]
    for i, values in enumerate(possible_fields):
        if field_name in values:
            pos_names[i] = field_name
            values.clear()

wanted_fields = {k for k, v in pos_names.items() if v.startswith("departure")}
wanted_my_ticket = [v for i, v in enumerate(my_ticket) if i in wanted_fields]

i = 1
for j in wanted_my_ticket:
    i *= j
print(i)
