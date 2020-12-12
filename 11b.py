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
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if (i, j) == (0, 0):
                    continue
                cur_i, cur_j = x+i, y+j
                while 0 <= cur_i < self.len_x and 0 <= cur_j < self.len_y:
                    cur = self.rows[cur_j][cur_i]
                    if cur != 0:
                        rtn.append(cur)
                        break
                    cur_i += i
                    cur_j += j
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
                elif new[y][x] == 2 and adjacent.count(2) >= 5:
                    new[y][x] = 1
                    changed = True
        self.rows = new
        return changed


with open("11.txt") as f:
    grid = Grid([[int(j == "L") for j in i.strip()]for i in f.readlines()])

while grid.update():
    print(grid, "\n")

print(grid.occupied)
