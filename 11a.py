from typing import List
from copy import deepcopy


class Grid:
    def __init__(self, rows):
        self.rows = rows

    def __str__(self):
        return "\n".join("".join(".L#"[j] for j in i) for i in self.rows)

    @property
    def len_x(self) -> int:
        return len(self.rows[0])

    @property
    def len_y(self) -> int:
        return len(self.rows)

    @property
    def occupied(self):
        return sum(self.rows[y][x] == 2 for x in range(self.len_x) for y in range(self.len_y))

    def adjacent(self, x, y) -> List[List[int]]:
        rtn = []
        for i in (x-1, x, x+1):
            for j in (y-1, y, y+1):
                if (i, j) == (x, y):
                    continue
                if 0 <= i < self.len_x and 0 <= j < self.len_y:
                    rtn.append(self.rows[j][i])
        return rtn

    def update(self) -> bool:
        changed = False
        new = deepcopy(self.rows)
        for x in range(self.len_x):
            for y in range(self.len_y):
                adjacent = self.adjacent(x, y)
                if new[y][x] == 1 and adjacent.count(2) == 0:
                    new[y][x] = 2
                    changed = True
                elif new[y][x] == 2 and adjacent.count(2) >= 4:
                    new[y][x] = 1
                    changed = True
        self.rows = new
        return changed


with open("11.txt") as f:
    grid = Grid([[int(j == "L") for j in i.strip()]for i in f.readlines()])


while grid.update():
    pass

print(grid.occupied)
