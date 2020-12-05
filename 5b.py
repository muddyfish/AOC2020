valid = 0

translation = str.maketrans("FBLR", "0101", "\n")
seat_ids = set()

with open("5.txt") as f:
    for i in f.readlines():
        seat_ids.add(int(i.translate(translation), 2))

min_id = min(seat_ids)
max_id = max(seat_ids)

print(set(range(min_id, max_id+1)) - seat_ids)