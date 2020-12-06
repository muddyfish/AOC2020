translation = str.maketrans("FBLR", "0101")

with open("5.txt") as f:
    data = f.read().translate(translation).split("\n")

print(int(max(data), 2))
