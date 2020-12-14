import re
set_regex = re.compile(r"mem\[(\d+)\] = (\d+)")

allow = 0
deny = 0

addresses = {}

allow_trans = str.maketrans("X01", "001")
deny_trans = str.maketrans("X01", "010")

with open("14.txt") as f:
    for i in f.readlines():
        i = i.strip()
        if i.startswith("mask = "):
            allow = int(i[7:].translate(allow_trans), 2)
            deny = int(i[7:].translate(deny_trans), 2)
        else:
            pos, value = map(int, set_regex.match(i).groups())
            addresses[pos] = (value | allow) & ~deny

print(sum(addresses.values()))
