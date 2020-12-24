from typing import Set, Tuple
from collections import defaultdict


def print_state():
    min_x, min_y, min_z = map(min, zip(*state))
    max_x, max_y, max_z = map(max, zip(*state))
    for z in range(min_z, max_z+1):
        print(f"\nz={z}")
        for y in range(min_y, max_y+1):
            print("".join(".#"[(x, y, z) in state] for x in range(min_x, max_x+1)))
    print()


def get_surroundings(ox, oy, oz) -> Set[Tuple[int, int, int]]:
    return {(x, y, z) for x in (ox-1, ox, ox+1) for y in (oy-1, oy, oy+1) for z in (oz-1, oz, oz+1)} - {(ox, oy, oz)}


def update_state(state):
    surrounding = defaultdict(lambda: 0)
    for pos in state:
        for adjacent in get_surroundings(*pos):
            surrounding[adjacent] += 1
        surrounding[pos] += 0
    state |= {pos for pos, count in surrounding.items() if count == 3}
    state -= {pos for pos, count in surrounding.items() if count not in {2, 3}}


with open("17.txt") as f:
    state = set((x, y, z) for z, rz in enumerate(f.read().split("\n\n")) for y, ry in enumerate(rz.split("\n")) for x, rx in enumerate(ry) if rx == "#")

for i in range(6):
    update_state(state)
    print(f"Cycle {i+1}")
    print_state()
print(len(state))
