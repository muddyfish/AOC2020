import re


field_regex = re.compile(
    r"(?P<byr>byr:\S+)|"
    r"(?P<iyr>iyr:\S+)|"
    r"(?P<eyr>eyr:\S+)|"
    r"(?P<hgt>hgt:\S+)|"
    r"(?P<hcl>hcl:\S+)|"
    r"(?P<ecl>ecl:\S+)|"
    r"(?P<pid>pid:\S+)|"
    r"(?P<cid>cid:\S+)"
)

valid = 0

with open("4.txt") as f:
    lines = [""]
    for i in f.readlines():
        i = i.strip()
        if i:
            lines[-1] += " " + i
        else:
            lines.append("")

ppd = []
for line in lines:
    ppd.append({m.lastgroup: m.group().replace(f"{m.lastgroup}:", "", 1) for m in field_regex.finditer(line)})

for pp in ppd:
    present = set(pp.keys()) - {"cid"}
    if len(present) >= 7:
        valid += 1

print(valid)
