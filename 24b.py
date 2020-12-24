from typing import Tuple, Set
from collections import Counter
import re
dir_regex = re.compile(r"(e|se|sw|w|nw|ne)")


def traverse_line(dirs) -> Tuple[int, int]:
    x = y = 0
    for dir in dirs:
        has_y = False
        if "n" in dir:
            y -= 1
            has_y = True
        elif "s" in dir:
            y += 1
            has_y = True
        if "e" in dir:
            x += 2 // (1 + has_y)
        elif "w" in dir:
            x -= 2 // (1 + has_y)
    return x, y


def get_adjacent(coord: Tuple[int, int]) -> Tuple[Tuple[int, int], ...]:
    x, y = coord
    return (
        (x+2, y),
        (x-2, y),
        (x+1, y+1),
        (x-1, y+1),
        (x+1, y-1),
        (x-1, y-1),
    )


def print_adjacency(coords: Set, adjacency: Counter):
    min_x, min_y = map(min, zip(*adjacency.keys()))
    max_x, max_y = map(max, zip(*adjacency.keys()))
    for y in range(min_y, max_y+1):
        print("".join(((x, y) in coords and "") or str(adjacency.get((x, y), "")) or " " for x in range(min_x, max_x+1)))
    print()


def run_tick(coords: Set[Tuple[int, int]]):
    adjacency = Counter()
    for coord in coords:
        adjacency.update(get_adjacent(coord))
        adjacency[coord] += 0
    #print_adjacency(coords, adjacency)
    for coord, count in adjacency.items():
        if coord in coords:
            # Black
            if count == 0 or count > 2:
                coords.discard(coord)
        else:
            if count == 2:
                coords.add(coord)


coords = set()
with open("24.txt") as f:
    for line in f.readlines():
        dirs = [m.group() for m in dir_regex.finditer(line.strip())]
        coords ^= {traverse_line(dirs)}


for i in range(100):
    run_tick(coords)
print(i+1, len(coords))
