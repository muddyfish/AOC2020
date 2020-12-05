translation = str.maketrans("FBLR", "0101", "\n")
seat_ids = set()

with open("5.txt") as f:
    for i in f.readlines():
        seat_ids.add(int(i.translate(translation), 2))

print(max(seat_ids))
