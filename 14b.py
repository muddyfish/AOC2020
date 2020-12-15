import re
set_regex = re.compile(r"mem\[(\d+)\] = (\d+)")

float_bits = []
addresses = {}
allow_trans = str.maketrans("X01", "001")


def set_float(bits, pos, value):
    if not bits:
        addresses[pos] = value
        return
    current, *rest = bits
    for i in [pos & ~current, pos | current]:
        set_float(rest, i, value)


with open("14.txt") as f:
    for i in f.readlines():
        i = i.strip()
        if i.startswith("mask = "):
            allow = int(i[7:].translate(allow_trans), 2)
            float_bits = [2**i for i, j in enumerate(i[:6:-1]) if j == "X"]
        else:
            pos, value = map(int, set_regex.match(i).groups())
            pos |= allow
            set_float(float_bits, pos, value)


print(sum(addresses.values()))
