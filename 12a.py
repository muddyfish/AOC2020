compass = "NESW"
faces = [(0, -1), (1, 0), (0, 1), (-1, 0)]
facing = 1
pos = [0, 0]

with open("12.txt") as f:
    for i in f.readlines():
        dir = i[0]
        amount = int(i.strip()[1:])
        if dir in compass:
            x, y = faces[compass.index(dir)]
        elif dir in "LR":
            x, y = 0, 0
            if dir == "L":
                facing -= amount // 90
            else:
                facing += amount // 90
            facing %= len(faces)
        else:
            x, y = faces[facing]
        pos[0] += amount * y
        pos[1] += amount * x

print(abs(pos[0]) + abs(pos[1]))
