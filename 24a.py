from typing import Tuple
from collections import defaultdict
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


coords = defaultdict(lambda: 0)
with open("24.txt") as f:
    for line in f.readlines():
        dirs = [m.group() for m in dir_regex.finditer(line.strip())]
        coords[traverse_line(dirs)] ^= 1

print(sum(coords.values()))

