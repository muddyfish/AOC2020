translation = str.maketrans("FBLR", "0101")

with open("BigBigDay5.txt") as f:
    data = f.read().translate(translation).split("\n")
seat_ids = {int(i, 2) for i in data}

min_id = int(min(data), 2)
max_id = int(max(data), 2)

for i in range(min_id, max_id+1):
    if i not in seat_ids:
        print(i)
        break
