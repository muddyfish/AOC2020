compass = "NESW"
faces = [(0, -1), (1, 0), (0, 1), (-1, 0)]
pos = [0, 0]
waypoint = [-1, 10]

with open("12.txt") as f:
    for i in f.readlines():
        dir = i[0]
        amount = int(i.strip()[1:])

        if dir in compass:
            wx, wy = faces[compass.index(dir)]
            waypoint[0] += amount * wy
            waypoint[1] += amount * wx
        elif dir in "LR":
            deg = amount // 90
            if dir == "L":
                deg *= -1
            deg %= 4
            if deg == 1:
                waypoint = [waypoint[1], -waypoint[0]]
            elif deg == 2:
                waypoint = [-waypoint[0], -waypoint[1]]
            elif deg == 3:
                waypoint = [-waypoint[1], waypoint[0]]
        else:
            pos[0] += amount * waypoint[0]
            pos[1] += amount * waypoint[1]

print(abs(pos[0]) + abs(pos[1]))
