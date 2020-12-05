translation = str.maketrans("FBLR", "0101", "\n")

with open("5.txt") as f:
    seat_ids = {int(i.translate(translation), 2) for i in f.readlines()}

min_id = min(seat_ids)
max_id = max(seat_ids)

for i in range(min_id, max_id+1):
    if i not in seat_ids:
        print(i)
